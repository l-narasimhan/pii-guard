"""Score a detector against labelled JSONL.

Recall    = of the real PII spans, how many were found   (misses = leaks)
Precision = of the spans flagged, how many were real PII  (false alarms = over-redaction)
A span counts as found if a prediction with the same label overlaps it.

    python -m pii.evaluate data/test.jsonl  [--out reports/m1_rules_test.md]
"""
import argparse
import json
import statistics
import time
from collections import defaultdict

from .rules import detect

RULE_LABELS = ["AADHAAR", "PAN", "GSTIN", "PHONE", "EMAIL", "UPI", "CARD", "BANK_ACCT",
               "PASSPORT", "VOTER_ID", "VEHICLE", "DOB", "IP"]
MODEL_LABELS = ["NAME", "ADDRESS"]


def overlaps(a, b):
    return a["start"] < b["end"] and b["start"] < a["end"]


def run(path, detector=detect):
    rows = [json.loads(l) for l in open(path)]
    tp = defaultdict(int); fn = defaultdict(int); fp = defaultdict(int)
    by_src = defaultdict(lambda: [0, 0])  # source -> [found, total] for rule labels
    misses, false_alarms, times = [], [], []
    chars = defaultdict(lambda: [0, 0])  # label -> [PII chars masked by any prediction, total PII chars]
    for ex in rows:
        t0 = time.perf_counter()
        pred = [{"start": s.start, "end": s.end, "label": s.label} for s in detector(ex["text"])]
        times.append((time.perf_counter() - t0) * 1000)
        masked = set()
        for p in pred:
            masked.update(range(p["start"], p["end"]))
        for g in ex["spans"]:
            span_chars = [i for i in range(g["start"], g["end"]) if not ex["text"][i].isspace()]
            chars[g["label"]][0] += sum(i in masked for i in span_chars)
            chars[g["label"]][1] += len(span_chars)
            hit = any(p["label"] == g["label"] and overlaps(p, g) for p in pred)
            (tp if hit else fn)[g["label"]] += 1
            if g["label"] in RULE_LABELS:
                by_src[ex["source"]][1] += 1
                by_src[ex["source"]][0] += hit
            if not hit and len(misses) < 40:
                misses.append((g["label"], ex["text"][g["start"]:g["end"]], ex["template"]))
        for p in pred:
            if not any(g["label"] == p["label"] and overlaps(p, g) for g in ex["spans"]):
                fp[p["label"]] += 1
                if len(false_alarms) < 40:
                    false_alarms.append((p["label"], ex["text"][p["start"]:p["end"]], ex["template"]))
    return rows, tp, fn, fp, by_src, misses, false_alarms, times, chars


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "–"


def report(path, detector=detect, title="Rule layer"):
    rows, tp, fn, fp, by_src, misses, false_alarms, times, chars = run(path, detector)
    L = [f"# {title}: {path}", "", f"{len(rows)} examples "
         f"({sum(r['source'] == 'chat' for r in rows)} chat, {sum(r['source'] == 'doc' for r in rows)} doc)", "",
         "| Label | Real spans | Found | Recall | False alarms | Precision |", "|---|---|---|---|---|---|"]
    other = sorted(set(tp) | set(fn) | set(fp) - set(RULE_LABELS) - set(MODEL_LABELS))
    other = [l for l in other if l not in RULE_LABELS and l not in MODEL_LABELS]
    for group, labels in [("rules", RULE_LABELS), ("model", MODEL_LABELS), ("other", other)]:
        for lab in labels:
            total = tp[lab] + fn[lab]
            if total or fp[lab]:
                L.append(f"| {lab} | {total} | {tp[lab]} | {pct(tp[lab], total)} | {fp[lab]} | {pct(tp[lab], tp[lab] + fp[lab])} |")
        if group == "rules":
            rt = sum(tp[l] + fn[l] for l in RULE_LABELS); rf = sum(tp[l] for l in RULE_LABELS)
            rp = sum(fp[l] for l in RULE_LABELS)
            L.append(f"| **Rule labels total** | {rt} | {rf} | **{pct(rf, rt)}** | {rp} | **{pct(rf, rf + rp)}** |")
    at = sum(tp.values()) + sum(fn.values()); af = sum(tp.values())
    L.append(f"| **All PII (incl. names/addresses)** | {at} | {af} | **{pct(af, at)}** | {sum(fp.values())} | |")
    cm = sum(c[0] for c in chars.values()); ct = sum(c[1] for c in chars.values())
    L += ["", f"**PII characters left visible (leak):** {pct(ct - cm, ct)} overall; "
          + ", ".join(f"{l} {pct(c[1] - c[0], c[1])}" for l, c in sorted(chars.items()) if c[1])]
    L += ["", "**Rule-label recall by source:** " + ", ".join(f"{s} {pct(f, t)}" for s, (f, t) in sorted(by_src.items())), ""]
    q = statistics.quantiles(times, n=100)
    L += [f"**Latency per message:** mean {statistics.mean(times):.3f} ms · p95 {q[94]:.3f} ms · p99 {q[98]:.3f} ms", ""]
    L += ["## Sample misses", ""] + [f"- {l}: `{v}` ({t})" for l, v, t in misses] or ["- none"]
    L += ["", "## Sample false alarms", ""] + ([f"- {l}: `{v}` ({t})" for l, v, t in false_alarms] or ["- none"])
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--out")
    a = ap.parse_args()
    text = report(a.path)
    print(text)
    if a.out:
        open(a.out, "w").write(text + "\n")
