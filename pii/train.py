"""Fine-tune a token classifier (tagger) for PII on our synthetic data.

Starts from a pretrained encoder, swaps its output layer for our 33 BIO tags,
and trains every weight (full fine-tune; the model is small enough).
Keeps the checkpoint with the lowest validation loss.

    .venv/bin/python -m pii.train --base microsoft/deberta-v3-base --out models/tagger-piiranha
    .venv/bin/python -m pii.train --smoke     # tiny CPU run to check the pipeline
"""
import argparse
import json
import math
import random
import time
from pathlib import Path

import torch
from transformers import AutoModelForTokenClassification, AutoTokenizer, get_linear_schedule_with_warmup

from .tagdata import IGNORE, TAG2ID, TAGS, encode


def load(path, tok, limit=None):
    rows = [json.loads(l) for l in open(path)][:limit]
    return [encode(r, tok) for r in rows]


def batches(items, size, shuffle, pad_id, rng):
    order = list(range(len(items)))
    if shuffle:
        rng.shuffle(order)
    for i in range(0, len(order), size):
        chunk = [items[j] for j in order[i:i + size]]
        n = max(len(c["input_ids"]) for c in chunk)
        n = 64 * math.ceil(n / 64)  # few fixed shapes: MPS caches memory per shape and won't release it
        ids = [c["input_ids"] + [pad_id] * (n - len(c["input_ids"])) for c in chunk]
        mask = [[1] * len(c["input_ids"]) + [0] * (n - len(c["input_ids"])) for c in chunk]
        labels = [c["labels"] + [IGNORE] * (n - len(c["labels"])) for c in chunk]
        yield torch.tensor(ids), torch.tensor(mask), torch.tensor(labels)


@torch.no_grad()
def valid_loss(model, items, device, pad_id, bs=64):
    model.eval()
    total, n = 0.0, 0
    for ids, mask, labels in batches(items, bs, False, pad_id, None):
        out = model(input_ids=ids.to(device), attention_mask=mask.to(device), labels=labels.to(device))
        total += out.loss.item() * len(ids)
        n += len(ids)
    model.train()
    return total / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="microsoft/deberta-v3-base")  # MIT; piiranha (CC BY-NC-ND) only for personal use
    ap.add_argument("--out", default="models/tagger")
    ap.add_argument("--epochs", type=float, default=3)
    ap.add_argument("--bs", type=int, default=16)
    ap.add_argument("--lr", type=float, default=5e-5)
    ap.add_argument("--eval-every", type=int, default=300)
    ap.add_argument("--smoke", action="store_true", help="64 examples, CPU, a few steps")
    ap.add_argument("--max-steps", type=int, default=0, help="stop early (speed/memory benchmark)")
    a = ap.parse_args()

    device = "cpu" if a.smoke else ("mps" if torch.backends.mps.is_available() else "cpu")
    rng = random.Random(0)
    torch.manual_seed(0)
    tok = AutoTokenizer.from_pretrained(a.base)
    model = AutoModelForTokenClassification.from_pretrained(
        a.base, num_labels=len(TAGS), id2label=dict(enumerate(TAGS)), label2id=TAG2ID,
        ignore_mismatched_sizes=True,  # new output layer for our tags
    ).to(device)

    limit = 64 if a.smoke else None
    train = load("data/train.jsonl", tok, limit)
    valid = load("data/valid.jsonl", tok, 32 if a.smoke else None)
    steps_per_epoch = math.ceil(len(train) / a.bs)
    total_steps = 4 if a.smoke else int(steps_per_epoch * a.epochs)
    if a.max_steps:
        total_steps = a.max_steps
    opt = torch.optim.AdamW(model.parameters(), lr=a.lr, weight_decay=0.01)
    sched = get_linear_schedule_with_warmup(opt, int(0.06 * total_steps), total_steps)
    print(f"device={device} base={a.base} train={len(train)} valid={len(valid)} steps={total_steps}")

    out = Path(a.out)
    best, step, t0, log = float("inf"), 0, time.time(), []
    model.train()
    while step < total_steps:
        for ids, mask, labels in batches(train, a.bs, True, tok.pad_token_id, rng):
            loss = model(input_ids=ids.to(device), attention_mask=mask.to(device), labels=labels.to(device)).loss
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step(); sched.step(); opt.zero_grad()
            step += 1
            if device == "mps" and step % 50 == 0:
                torch.mps.empty_cache()
            if step % 50 == 0 or a.smoke or (a.max_steps and step % 10 == 0):
                mem = f" mps {torch.mps.current_allocated_memory() / 1e9:.1f}GB" if device == "mps" else ""
                print(f"step {step}/{total_steps} loss {loss.item():.4f} ({time.time() - t0:.0f}s){mem}", flush=True)
            if step % a.eval_every == 0 or step == total_steps:
                vl = valid_loss(model, valid, device, tok.pad_token_id)
                log.append({"step": step, "train_loss": loss.item(), "valid_loss": vl, "secs": round(time.time() - t0)})
                flag = ""
                if vl < best:
                    best = vl
                    model.save_pretrained(out); tok.save_pretrained(out)
                    flag = "  <- saved"
                print(f"   valid loss {vl:.4f}{flag}", flush=True)
            if step >= total_steps:
                break
    out.mkdir(parents=True, exist_ok=True)
    json.dump({"base": a.base, "epochs": a.epochs, "lr": a.lr, "bs": a.bs, "best_valid_loss": best,
               "minutes": round((time.time() - t0) / 60, 1), "log": log}, open(out / "train_log.json", "w"), indent=1)
    print(f"done: best valid loss {best:.4f} -> {out} ({(time.time() - t0) / 60:.1f} min)")


if __name__ == "__main__":
    main()
