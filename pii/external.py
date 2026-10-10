"""Score the engine on independent public Indian PII benchmarks (not written by us).

- Ylemis India-PII Benchmark (CC0): 10,000 cases, 16 types, 14 language/format slices.
- Maskara Indian PII (MIT): real_world_eval (2,600) + template_disjoint_eval (en-IN, hi-IN rows).

Their label sets differ from ours, so:
  in scope   -> scored (leak = PII characters left unmasked, whatever label we gave)
  gap        -> PII we don't model yet (medical_id, account_id, secrets): scored, reported separately
  ignore     -> not PII under our design (organization, location, IFSC, US SSN): neither a miss
                nor a false alarm if we flag it

    .venv/bin/python -m pii.external models/tagger-piiranha
"""
import json
import re
import statistics
import sys
import time
from collections import defaultdict

YLEMIS = {
    "person": "in", "indian_phone": "in", "address": "in", "pan": "in", "aadhaar": "in", "upi_id": "in",
    "email": "in", "voter_id": "in", "vehicle_registration": "in", "gstin": "in", "indian_passport": "in",
    "account_id": "gap", "medical_id": "gap",
    "location": "ignore", "organization": "ignore", "ifsc": "ignore",
}
MASKARA = {
    "PERSON_NAME": "in", "PHONE": "in", "AADHAAR": "in", "EMAIL": "in", "UPI_ID": "in", "PAN_CARD": "in",
    "ADDRESS": "in", "VEHICLE_REG": "in", "DRIVER_LICENSE": "in", "IP_ADDRESS": "in", "DATE_OF_BIRTH": "in",
    "PASSPORT": "in", "CREDIT_CARD": "in",
    "USERNAME": "gap", "API_KEY": "gap", "PASSWORD": "gap",
    "SSN": "ignore",
}
# label words some datasets include inside the span ("Aadhaar No. 0967…", "Ms. Gaurav Mitra")
PREFIX = re.compile(r"^(?:aadhaar(?: no\.?| number)?[:\s]*|uid[:\s]*|pan[:\s]*|(?:mr|ms|mrs|dr|smt|shri|sri)\.?\s+)", re.I)


def script(text):
    return "indic" if any(0x0900 <= ord(c) < 0x0E00 for c in text) else "latin"


def load_ylemis():
    for r in map(json.loads, open("data/external/ylemis.jsonl")):
        yield {"text": r["text"], "slice": r["language"], "cat": r["category"], "src": "ylemis",
               "gold": [(e["start"], e["end"], e["type"], YLEMIS[e["type"]]) for e in r["entities"]]}


def load_maskara(name, locales=("en-IN", "hi-IN")):
    import pyarrow.parquet as pq
    for r in pq.read_table(f"data/external/{name}.parquet").to_pylist():
        if r["locale"] not in locales:
            continue
        yield {"text": r["text"], "slice": r["domain"], "cat": r["difficulty"], "src": name,
               "gold": [(e["start"], e["end"], e["label"], MASKARA[e["label"]]) for e in r["entities"]]}


def value_chars(text, s, e):
    m = PREFIX.match(text[s:e])
    s += m.end() if m else 0
    return [i for i in range(s, e) if text[i].isalnum()]


def score(rows, detector):
    agg = defaultdict(lambda: [0, 0, 0, 0])  # key -> [masked chars, total chars, spans found, spans]
    neg_docs = neg_flagged = 0
    fps, fp_examples, times = 0, [], []
    for ex in rows:
        t0 = time.perf_counter()
        pred = detector(ex["text"])
        times.append((time.perf_counter() - t0) * 1000)
        masked = set()
        for p in pred:
            masked.update(range(p.start, p.end))
        scored = [(s, e, lab, k) for s, e, lab, k in ex["gold"] if k != "ignore"]
        for s, e, lab, kind in scored:
            chars = value_chars(ex["text"], s, e)
            m = sum(i in masked for i in chars)
            hit = any(p.start < e and s < p.end for p in pred)
            for key in (f"{kind}:{lab}", f"{kind}:ALL", f"slice:{ex['src']}:{ex['slice']}:{kind}"):
                a = agg[key]; a[0] += m; a[1] += len(chars); a[2] += hit; a[3] += 1
        for p in pred:  # false alarm = flagged text overlapping no gold span at all (incl. ignored ones)
            if not any(p.start < e and s < p.end for s, e, _, _ in ex["gold"]):
                fps += 1
                if len(fp_examples) < 25:
                    fp_examples.append((p.label, ex["text"][p.start:p.end], ex["cat"]))
        if not ex["gold"]:
            neg_docs += 1
            neg_flagged += bool(pred)
    return agg, fps, fp_examples, neg_docs, neg_flagged, times


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "–"


def report(name, rows, detector):
    agg, fps, fpx, nd, nf, times = score(rows, detector)
    L = [f"## {name}: {len(rows)} texts", "",
         "| Group | Spans | Found (any label) | **Leak** (chars unmasked) |", "|---|---|---|---|"]
    for key in sorted(k for k in agg if not k.startswith("slice:")):
        m, c, h, n = agg[key]
        bold = "**" if key.endswith(":ALL") else ""
        L.append(f"| {bold}{key}{bold} | {n} | {pct(h, n)} | {bold}{pct(c - m, c)}{bold} |")
    L += ["", f"**False alarms:** {fps} flagged spans overlapping no labelled entity; "
          f"PII-free texts with any flag: {nf}/{nd} ({pct(nf, nd)})",
          f"**Latency:** mean {statistics.mean(times):.1f} ms · p95 {statistics.quantiles(times, n=20)[18]:.1f} ms", "",
          "| Slice (in-scope PII) | Spans | Found | Leak |", "|---|---|---|---|"]
    for key in sorted(k for k in agg if k.startswith("slice:") and k.endswith(":in")):
        m, c, h, n = agg[key]
        L.append(f"| {key[6:-3]} | {n} | {pct(h, n)} | {pct(c - m, c)} |")
    L += ["", "Sample false alarms:"] + [f"- {l}: `{v}` ({c})" for l, v, c in fpx]
    return "\n".join(L)


if __name__ == "__main__":
    from .tagger import Tagger, engine

    model = sys.argv[1] if len(sys.argv) > 1 else "models/tagger-piiranha"
    det = engine(Tagger(model))
    ylemis = list(load_ylemis())
    sets = [
        ("Ylemis: Latin-script slices (our scope)", [r for r in ylemis if script(r["text"]) == "latin"]),
        ("Ylemis: native-script slices (out of scope)", [r for r in ylemis if script(r["text"]) == "indic"]),
        ("Maskara real_world_eval (en-IN)", list(load_maskara("maskara_real"))),
        ("Maskara template_disjoint_eval (en-IN + hi-IN)", list(load_maskara("maskara_disjoint"))),
    ]
    out = ["# External benchmarks: Rules + tagger", f"model: `{model}`", ""]
    for name, rows in sets:
        print(f"scoring {name} ({len(rows)})", file=sys.stderr, flush=True)
        out.append(report(name, rows, det))
        out.append("")
        print(out[-2].split("\n\n")[0], flush=True)
    open("reports/m3_external.md", "w").write("\n".join(out) + "\n")
    print("-> reports/m3_external.md")
