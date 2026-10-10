"""Convert data/handwritten.txt ([[LABEL:value]] markup) into JSONL with spans.

    python -m pii.handwritten     # -> data/handwritten.jsonl
"""
import json
import re

MARK = re.compile(r"\[\[([A-Z_]+):(.+?)\]\]")


def parse_item(block: str) -> dict:
    lines = block.strip("\n").split("\n")
    source = lines[0].lstrip("@").strip()
    raw = "\n".join(lines[1:])
    text, spans, cursor = [], [], 0
    pos = 0
    for m in MARK.finditer(raw):
        lit = raw[cursor:m.start()]
        text.append(lit); pos += len(lit)
        value = m.group(2)
        spans.append({"start": pos, "end": pos + len(value), "label": m.group(1)})
        text.append(value); pos += len(value)
        cursor = m.end()
    text.append(raw[cursor:])
    return {"text": "".join(text), "spans": spans, "source": source, "template": "handwritten"}


def main(src="data/handwritten.txt", out="data/handwritten.jsonl"):
    body = "\n".join(l for l in open(src).read().split("\n") if not l.startswith("#"))
    items = [parse_item(b) for b in body.split("\n---\n") if b.strip()]
    with open(out, "w") as f:
        for i, ex in enumerate(items):
            ex["id"] = f"hw-{i:03d}"
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    n_spans = sum(len(e["spans"]) for e in items)
    print(f"{len(items)} items ({sum(e['source'] == 'chat' for e in items)} chat, "
          f"{sum(e['source'] == 'doc' for e in items)} doc), {n_spans} PII spans, "
          f"{sum(not e['spans'] for e in items)} with no PII -> {out}")


if __name__ == "__main__":
    main()
