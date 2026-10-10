"""Build chat-format fine-tuning data for Gemma (mlx-lm LoRA) from our labelled JSONL.

Short instruction in, compact JSON out: [["Divya","NAME"],["98450 12345","PHONE"]].
A short prompt and compact answer mean fewer tokens, which means faster inference.

    .venv/bin/python -m pii.gemma_sft        # -> data/sft/{train,valid}.jsonl
"""
import json
from pathlib import Path

INSTRUCTION = "Extract personal data (PII) from the text. Answer as a JSON list of [value, LABEL]; [] if none.\n\nText:\n"


def target(ex: dict) -> str:
    seen, out = set(), []
    for sp in sorted(ex["spans"], key=lambda s: s["start"]):
        item = (ex["text"][sp["start"]:sp["end"]], sp["label"])
        if item not in seen:
            seen.add(item)
            out.append(list(item))
    return json.dumps(out, ensure_ascii=False, separators=(",", ":"))


def to_chat(ex: dict) -> dict:
    return {"messages": [{"role": "user", "content": INSTRUCTION + ex["text"]},
                         {"role": "assistant", "content": target(ex)}]}


def main(out_dir="data/sft"):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for split, n in [("train", None), ("valid", 300)]:  # mlx evaluates the whole valid file: keep it small
        rows = [json.loads(l) for l in open(f"data/{split}.jsonl")][:n]
        with open(out / f"{split}.jsonl", "w") as f:
            for ex in rows:
                f.write(json.dumps(to_chat(ex), ensure_ascii=False) + "\n")
        print(f"{split}: {len(rows)} -> {out / f'{split}.jsonl'}")
    print("example:", json.dumps(to_chat(json.loads(open("data/train.jsonl").readline())), ensure_ascii=False)[:400])


if __name__ == "__main__":
    main()
