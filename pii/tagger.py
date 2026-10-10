"""Run a trained tagger, and the full engine (rules first, tagger fills gaps).

    .venv/bin/python -m pii.tagger models/tagger-piiranha data/handwritten.jsonl data/test.jsonl
"""
import re
import sys

from .rules import RE_IP, RE_IP6, Span, detect, phone_context_ok, resolve_overlaps
from .tagdata import decode


class Tagger:
    """PyTorch runtime (training/eval). Serving uses pii.onnx_tagger.OnnxTagger (no PyTorch needed)."""

    def __init__(self, path: str, device: str = "cpu"):
        from transformers import AutoModelForTokenClassification, AutoTokenizer
        self.name = f"tagger({path.rstrip('/').split('/')[-1]})"
        self.tok = AutoTokenizer.from_pretrained(path)
        self.model = AutoModelForTokenClassification.from_pretrained(path).to(device).eval()
        self.device = device

    def __call__(self, text: str) -> list[Span]:
        import torch
        with torch.no_grad():
            return self._predict(text)

    def _predict(self, text: str) -> list[Span]:
        # long texts: overlapping 384-token windows, later windows overwrite earlier tags
        enc = self.tok(text, truncation=True, max_length=384, stride=64, return_overflowing_tokens=True,
                       return_offsets_mapping=True, return_tensors="pt", padding=True)
        offsets = enc.pop("offset_mapping")
        enc.pop("overflow_to_sample_mapping", None)
        logits = self.model(**{k: v.to(self.device) for k, v in enc.items()}).logits.argmax(-1).cpu()
        by_char: dict[tuple, int] = {}
        for win_off, win_tags in zip(offsets.tolist(), logits.tolist()):
            for off, t in zip(win_off, win_tags):
                if off[0] != off[1]:
                    by_char[tuple(off)] = t
        offs = sorted(by_char)
        return decode(text, offs, [by_char[o] for o in offs])


NUM_WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|shunya|ek|do|teen|chaar|paanch|chhe|saat|aath|nau)\b", re.I)


FORMATS = {  # structured labels: what the value itself must look like
    "VOTER_ID": lambda v: re.fullmatch(r"[A-Z]{3}\d{7}", v, re.I),
    "PASSPORT": lambda v: re.fullmatch(r"[A-Z]\d{7}", v, re.I),
    "PAN": lambda v: re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", v, re.I),
    "AADHAAR": lambda v: re.fullmatch(r"\d{12}", v),
    "BANK_ACCT": lambda v: re.fullmatch(r"\d{9,18}", v),
    "CARD": lambda v: re.fullmatch(r"\d{13,19}", v),
    "VEHICLE": lambda v: re.fullmatch(r"[A-Z]{2}\d{1,2}[A-Z]{0,3}\d{4}", v, re.I),
}


def plausible(text: str, sp: Span, others: list[Span]) -> Span | None:
    """Format sanity checks on tagger output: the tagger is good at context, not at formats.
    A span that fails its own label's format is relabelled if it fits another; kept as a generic
    unverified "ID" if it still looks like one (6+ digits); dropped otherwise."""
    v = text[sp.start:sp.end]
    compact = re.sub(r"[\s-]", "", v)
    alnum = sum(c.isalnum() for c in v)
    digits = sum(c.isdigit() for c in v)
    if alnum < 3:
        return None                       # fragments: "ph", "78"
    if sp.label == "PHONE":
        if len(NUM_WORDS.findall(v)) >= 5:
            return sp                     # spoken digits
        if not phone_context_ok(text, sp.start):
            return None
        if digits >= 8:
            return sp
        near = any(o is not sp and o.label == "PHONE" and abs(o.start - sp.end) < 60 for o in others)
        return sp if digits >= 4 and near else None   # one half of a split number
    if sp.label == "IP":
        return sp if RE_IP.fullmatch(v) or RE_IP6.fullmatch(v) else None
    if sp.label in FORMATS:
        if FORMATS[sp.label](compact):
            return sp
        for lab, ok in FORMATS.items():
            if ok(compact) and not (compact.isdigit() and lab in ("BANK_ACCT", "CARD")):
                return Span(sp.start, sp.end, lab, sp.source)   # e.g. a voter ID the model called Aadhaar
        # fits no known format: still mask anything that looks like an ID number (recall first),
        # but label it honestly as an unverified ID; drop short letter-heavy codes like "LCXC2KNH"
        return Span(sp.start, sp.end, "ID", sp.source) if digits >= 6 else None
    return sp


NAME_CUE = re.compile(r"(?:\bname\s+is|\bnaam\s+(?:hai\s+)?|\bmera\s+naam|\bi\s+am|\bi'm|\bthis\s+is|\bmy\s+name)\s*:?\s*$", re.I)
STOP = {"and", "while", "but", "or", "here", "hai", "hoon", "hu", "is", "ka", "ki", "ke", "se", "from", "my", "mera",
        "the", "please", "pls", "plz", "speaking", "bol", "raha", "rahi", "number", "no", "phone", "mobile", "order",
        "address", "aur", "ji", "sir", "madam", "this", "at", "on", "in", "for", "with", "to"}


def widen(text: str, sp: Span) -> Span:
    """Never cut a word in half: grow the span to whole-word boundaries."""
    while sp.start > 0 and text[sp.start - 1].isalnum() and text[sp.start].isalnum():
        sp.start -= 1
    while sp.end < len(text) and text[sp.end].isalnum() and text[sp.end - 1].isalnum():
        sp.end += 1
    return sp


def extend_name(text: str, sp: Span, max_words: int = 4) -> Span:
    """After an explicit cue ("name is", "mera naam"), carry the name over following words
    until a stop word, punctuation or digit."""
    if sp.label != "NAME" or not NAME_CUE.search(text[max(0, sp.start - 25):sp.start]):
        return sp
    for _ in range(max_words):
        m = re.match(r"\s+([^\W\d_][\w.'-]*)", text[sp.end:])
        if not m or m.group(1).lower() in STOP:
            break
        sp.end += m.end()
    return sp


def engine(tagger, postfilter: bool = True):
    """Rules win (checksum/context verified); tagger adds what doesn't overlap them,
    after format sanity checks."""
    def detect_all(text):
        rule = detect(text)
        tagged = [widen(text, t) for t in tagger(text)]
        tagged = [extend_name(text, t) for t in tagged]
        if postfilter:
            tagged = [p for p in (plausible(text, t, tagged) for t in tagged) if p]
        extra = [m for m in tagged if all(m.end <= r.start or m.start >= r.end for r in rule)]
        return resolve_overlaps(rule + extra)
    return detect_all


if __name__ == "__main__":
    from .evaluate import report

    path, sets = sys.argv[1], sys.argv[2:] or ["data/handwritten.jsonl"]
    t = Tagger(path)
    tag = path.rstrip("/").split("/")[-1].replace("-", "_")
    for ds in sets:
        split = ds.split("/")[-1].replace(".jsonl", "")
        for det, title in [(t, t.name), (engine(t), f"Rules + {t.name}")]:
            text = report(ds, det, title=title)
            out = f"reports/m3_{'engine_' if title.startswith('Rules') else ''}{tag}_{split}.md"
            open(out, "w").write(text + "\n")
            print(f"\n=== {title} on {split} -> {out}")
            for line in text.split("\n"):
                if line.startswith("| **") or line.startswith("**PII") or line.startswith("**Latency") \
                        or line.startswith("| NAME") or line.startswith("| ADDRESS") or line.startswith("| PHONE"):
                    print(line)
