"""Off-the-shelf PII models as baselines, mapped onto our labels.

- GLiNER-PII: zero-shot; we pass label names in plain English.
- Piiranha: DeBERTa token classifier trained on (mostly Western) PII.

    .venv/bin/python -m pii.baselines data/handwritten.jsonl data/test.jsonl
"""
import sys
import time

from .rules import Span, detect, resolve_overlaps

GLINER_LABELS = {
    "person name": "NAME", "address": "ADDRESS", "phone number": "PHONE", "email": "EMAIL",
    "upi id": "UPI", "aadhaar number": "AADHAAR", "pan number": "PAN", "gstin": "GSTIN",
    "credit card number": "CARD", "bank account number": "BANK_ACCT", "passport number": "PASSPORT",
    "voter id": "VOTER_ID", "vehicle registration number": "VEHICLE", "date of birth": "DOB",
    "ip address": "IP", "driving licence number": "DL",
}
PIIRANHA_LABELS = {
    "GIVENNAME": "NAME", "SURNAME": "NAME", "STREET": "ADDRESS", "BUILDINGNUM": "ADDRESS",
    "CITY": "ADDRESS", "ZIPCODE": "ADDRESS", "TELEPHONENUM": "PHONE", "EMAIL": "EMAIL",
    "CREDITCARDNUMBER": "CARD", "ACCOUNTNUM": "BANK_ACCT", "DATEOFBIRTH": "DOB",
    "DRIVERLICENSENUM": "DL", "IDCARDNUM": "AADHAAR", "SOCIALNUM": "AADHAAR", "TAXNUM": "PAN",
}


def merge_adjacent(spans: list[Span], text: str, gap: str = " ,") -> list[Span]:
    """Join same-label pieces split only by spaces/commas (GIVENNAME+SURNAME -> NAME)."""
    out: list[Span] = []
    for s in sorted(spans, key=lambda s: s.start):
        if out and out[-1].label == s.label and all(c in gap for c in text[out[-1].end:s.start]):
            out[-1] = Span(out[-1].start, s.end, s.label, s.source)
        else:
            out.append(s)
    return out


class Gliner:
    name = "GLiNER-PII"

    def __init__(self, model_id="urchade/gliner_multi_pii-v1", threshold=0.4):
        from gliner import GLiNER
        self.model = GLiNER.from_pretrained(model_id)
        self.threshold = threshold

    def __call__(self, text: str) -> list[Span]:
        ents = self.model.predict_entities(text, list(GLINER_LABELS), threshold=self.threshold)
        return [Span(e["start"], e["end"], GLINER_LABELS[e["label"]], "gliner") for e in ents]


class Piiranha:
    name = "Piiranha"

    def __init__(self, model_id="iiiorg/piiranha-v1-detect-personal-information"):
        from transformers import pipeline
        self.pipe = pipeline("token-classification", model=model_id, aggregation_strategy="simple", device="cpu")

    def __call__(self, text: str) -> list[Span]:
        spans = []
        for e in self.pipe(text):
            lab = PIIRANHA_LABELS.get(e["entity_group"].replace("I-", "").replace("B-", ""))
            if lab:
                spans.append(Span(e["start"], e["end"], lab, "piiranha"))
        return merge_adjacent(spans, text)


def combined(model):
    """Rule spans are checksum/context-verified, so they win; the model only adds
    spans that don't overlap any rule span (names, addresses, odd formats)."""
    def detect_both(text):
        rule = detect(text)
        extra = [m for m in model(text) if all(m.end <= r.start or m.start >= r.end for r in rule)]
        return resolve_overlaps(rule + extra)
    detect_both.name = f"Rules + {model.name}"
    return detect_both


if __name__ == "__main__":
    from .evaluate import report

    paths = sys.argv[1:] or ["data/handwritten.jsonl"]
    for cls in (Gliner, Piiranha):
        t0 = time.time()
        model = cls()
        print(f"loaded {cls.name} in {time.time() - t0:.0f}s", file=sys.stderr)
        for path in paths:
            for det, title in [(model, model.name), (combined(model), f"Rules + {model.name}")]:
                tag = title.lower().replace(" + ", "_plus_").replace("-", "_").replace(" ", "_")
                split = path.split("/")[-1].replace(".jsonl", "")
                out = f"reports/m2_{tag}_{split}.md"
                text = report(path, det, title=title)
                open(out, "w").write(text + "\n")
                print(f"\n=== {title} on {split} -> {out}")
                for line in text.split("\n"):
                    if line.startswith("|") or line.startswith("**"):
                        print(line)
