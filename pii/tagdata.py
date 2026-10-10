"""Char spans <-> per-token BIO tags for a token-classification model.

Each word piece gets one tag: B-LABEL (first piece of a PII span), I-LABEL
(continuation) or O. A piece belongs to a span if it overlaps the span
(pieces can straddle the edge, e.g. "=203" in "ip=203.35.47.242"); decoded
spans are trimmed of edge punctuation.

    .venv/bin/python -m pii.tagdata     # alignment check on train/valid/test/handwritten
"""
import json

from .rules import Span

ENTITY_LABELS = ["NAME", "ADDRESS", "PHONE", "EMAIL", "UPI", "AADHAAR", "PAN", "GSTIN", "CARD",
                 "BANK_ACCT", "PASSPORT", "VOTER_ID", "VEHICLE", "DOB", "IP", "DL"]
TAGS = ["O"] + [f"{p}-{l}" for l in ENTITY_LABELS for p in ("B", "I")]
TAG2ID = {t: i for i, t in enumerate(TAGS)}
IGNORE = -100  # special tokens: not scored in the loss


def piece_start(text: str, start: int, end: int) -> int:
    while start < end and text[start].isspace():
        start += 1
    return start


def encode(example: dict, tokenizer, max_len: int = 384) -> dict:
    enc = tokenizer(example["text"], truncation=True, max_length=max_len, return_offsets_mapping=True)
    tags, prev_span = [], None
    for (s, e) in enc["offset_mapping"]:
        if s == e:  # [CLS]/[SEP]
            tags.append(IGNORE)
            prev_span = None
            continue
        s = piece_start(example["text"], s, e)
        span = next((sp for sp in example["spans"] if s < sp["end"] and sp["start"] < e), None)
        if span is None:
            tags.append(TAG2ID["O"])
        else:
            prefix = "I" if span is prev_span else "B"
            tags.append(TAG2ID[f"{prefix}-{span['label']}"])
        prev_span = span
    enc.pop("offset_mapping")
    enc["labels"] = tags
    return enc


LEAD_PUNCT = "=(:[,;\"'|/"
TRAIL_PUNCT = ")],;:\"'.|/"


def trim(text: str, sp: Span) -> Span:
    while sp.start < sp.end and (text[sp.start] in LEAD_PUNCT or text[sp.start].isspace()):
        sp.start += 1
    while sp.end > sp.start and (text[sp.end - 1] in TRAIL_PUNCT or text[sp.end - 1].isspace()):
        sp.end -= 1
    return sp


def decode(text: str, offsets: list, tag_ids: list) -> list[Span]:
    """Per-token tags -> char spans. An I- without a preceding B- still opens a span."""
    spans: list[Span] = []
    cur = None
    for (s, e), t in zip(offsets, tag_ids):
        if s == e:
            continue
        tag = TAGS[t]
        s = piece_start(text, s, e)
        if tag == "O":
            cur = None
            continue
        kind, label = tag.split("-", 1)
        # continue on I-, or on a B- glued to the previous piece (no space): "Div"+"ya"
        if cur is not None and cur.label == label and (kind == "I" or s == cur.end):
            cur.end = e
        else:
            cur = Span(s, e, label, "tagger")
            spans.append(cur)
    return [sp for sp in (trim(text, sp) for sp in spans) if sp.end > sp.start]


if __name__ == "__main__":
    from transformers import AutoTokenizer

    tok = AutoTokenizer.from_pretrained("iiiorg/piiranha-v1-detect-personal-information")
    for path in ["data/train.jsonl", "data/valid.jsonl", "data/test.jsonl", "data/handwritten.jsonl"]:
        rows = [json.loads(l) for l in open(path)]
        exact = total = truncated = 0
        lengths = []
        bad = []
        for ex in rows:
            enc = tok(ex["text"], truncation=True, max_length=384, return_offsets_mapping=True)
            lengths.append(len(enc["input_ids"]))
            truncated += len(tok(ex["text"])["input_ids"]) > 384
            got = {(s.start, s.end, s.label) for s in decode(ex["text"], enc["offset_mapping"], encode(ex, tok)["labels"])}
            for sp in ex["spans"]:
                total += 1
                # gold span with surrounding whitespace trimmed
                g = trim(ex["text"], Span(sp["start"], sp["end"], sp["label"]))
                if (g.start, g.end, g.label) in got:
                    exact += 1
                elif len(bad) < 5:
                    bad.append((sp["label"], ex["text"][sp["start"]:sp["end"]]))
        print(f"{path}: {len(rows)} ex, spans recoverable exactly {exact}/{total} ({100 * exact / total:.2f}%), "
              f"max tokens {max(lengths)}, truncated {truncated}")
        for b in bad:
            print("   not exact:", b)
