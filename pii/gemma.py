"""Gemma (generative LLM) as a zero-shot PII detector, scored like the other baselines.

We *ask* Gemma to list PII as JSON [{"text": ..., "label": ...}], then find each
returned string in the input to get character spans. Unlike a tagger, a
generative model can return text that isn't in the input (hallucination); those
are dropped and counted.

    .venv/bin/python -m pii.gemma mlx-community/gemma-4-e2b-it-4bit data/handwritten.jsonl
"""
import json
import re
import sys
import time

from mlx_lm import generate, load

from .rules import Span, detect, resolve_overlaps

LABELS = {
    "NAME": "a person's name (full or first name only)",
    "ADDRESS": "a home/office/delivery address or location description of where a person lives or works",
    "PHONE": "a person's phone number in any format (spaces, words, country code, landline)",
    "EMAIL": "a personal email address",
    "UPI": "a UPI payment ID like name@bank",
    "AADHAAR": "a 12-digit Aadhaar number",
    "PAN": "a PAN number (10 characters like ABCDE1234F)",
    "GSTIN": "a 15-character GST number",
    "CARD": "a payment card number",
    "BANK_ACCT": "a bank account number",
    "PASSPORT": "a passport number",
    "VOTER_ID": "a voter ID / EPIC number",
    "VEHICLE": "a vehicle registration number",
    "DOB": "a date of birth",
    "IP": "an IP address",
    "DL": "a driving licence number",
}

PROMPT = """Find all personal data (PII) in the text below. Labels:
{labels}

Rules:
- Copy each PII value EXACTLY as it appears in the text (same spelling, spaces, case).
- Do not include titles like Mr./Dr. in names.
- Business names, festivals, products, order/tracking/invoice numbers, IFSC codes, toll-free numbers and masked values (like XXXX 1234) are NOT PII.
- If there is no PII, return [].

Return ONLY a JSON array like [{{"text": "...", "label": "NAME"}}].

Text:
\"\"\"
{text}
\"\"\""""


class Gemma:
    def __init__(self, model_id: str, max_tokens: int = 512, adapter: str | None = None):
        self.model_id = model_id
        self.adapter = adapter
        self.name = model_id.split("/")[-1] + ("+lora" if adapter else "")
        self.model, self.tok = load(model_id, adapter_path=adapter) if adapter else load(model_id)
        self.max_tokens = max_tokens
        self.stats = {"calls": 0, "returned": 0, "not_in_text": 0, "bad_json": 0, "bad_label": 0}

    def prompt(self, text: str) -> str:
        if self.adapter:  # fine-tuned: same short instruction + default template as in training
            from .gemma_sft import INSTRUCTION
            msgs = [{"role": "user", "content": INSTRUCTION + text}]
            return self.tok.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False)
        labels = "\n".join(f"- {k}: {v}" for k, v in LABELS.items())
        msgs = [{"role": "user", "content": PROMPT.format(labels=labels, text=text)}]
        try:
            return self.tok.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False, enable_thinking=False)
        except TypeError:
            return self.tok.apply_chat_template(msgs, add_generation_prompt=True, tokenize=False)

    def raw(self, text: str) -> str:
        return generate(self.model, self.tok, prompt=self.prompt(text), max_tokens=self.max_tokens)

    def __call__(self, text: str) -> list[Span]:
        self.stats["calls"] += 1
        out = self.raw(text)
        m = re.search(r"\[.*\]", out, re.S)
        try:
            items = json.loads(m.group()) if m else []
        except json.JSONDecodeError:
            self.stats["bad_json"] += 1
            items = []
        spans = []
        for it in items if isinstance(items, list) else []:
            if isinstance(it, list) and len(it) == 2:  # compact fine-tuned format [value, LABEL]
                it = {"text": it[0], "label": it[1]}
            if not isinstance(it, dict):
                continue
            val, lab = str(it.get("text", "")).strip(), str(it.get("label", "")).upper()
            if not val:
                continue
            self.stats["returned"] += 1
            if lab not in LABELS:
                self.stats["bad_label"] += 1
                continue
            found = [mm.start() for mm in re.finditer(re.escape(val), text)] or \
                    [mm.start() for mm in re.finditer(re.escape(val), text, re.I)]
            if not found:
                self.stats["not_in_text"] += 1  # hallucinated or altered value
            for st in found:
                spans.append(Span(st, st + len(val), lab, "gemma"))
        return resolve_overlaps(spans)


def combined(model):
    def detect_both(text):
        rule = detect(text)
        extra = [m for m in model(text) if all(m.end <= r.start or m.start >= r.end for r in rule)]
        return resolve_overlaps(rule + extra)
    return detect_both


if __name__ == "__main__":
    import json as _json
    import random

    from .evaluate import report

    args = sys.argv[1:]
    adapter = None
    if "--adapter" in args:
        i = args.index("--adapter"); adapter = args[i + 1]; del args[i:i + 2]
    model_id, paths = args[0], args[1:] or ["data/handwritten.jsonl"]
    t0 = time.time()
    g = Gemma(model_id, adapter=adapter)
    print(f"loaded {g.name} in {time.time() - t0:.0f}s", file=sys.stderr)
    for path in paths:
        if "test.jsonl" in path:  # 1,500 is slow for an LLM: fixed random 300
            rows = [l for l in open(path)]
            random.Random(0).shuffle(rows)
            path_s = path.replace(".jsonl", "_sample300.jsonl")
            open(path_s, "w").writelines(rows[:300])
            path = path_s
        split = path.split("/")[-1].replace(".jsonl", "")
        cache: dict[str, list[Span]] = {}

        def cached(text):  # run Gemma once per text; reuse for the combined score
            if text not in cache:
                cache[text] = g(text)
            return cache[text]
        cached.name = g.name
        for det, title in [(cached, g.name), (combined(cached), f"Rules + {g.name}")]:
            text = report(path, det, title=title)
            out = f"reports/m2_{title.lower().replace(' + ', '_plus_').replace('-', '_').replace(' ', '_')}_{split}.md"
            open(out, "w").write(text + f"\n\nGemma stats: {_json.dumps(g.stats)}\n")
            print(f"\n=== {title} on {split} -> {out}")
            for line in text.split("\n"):
                if line.startswith("| **") or line.startswith("**PII") or line.startswith("**Latency") \
                        or line.startswith("| NAME") or line.startswith("| ADDRESS") or line.startswith("| PHONE"):
                    print(line)
        print("stats", g.stats)
