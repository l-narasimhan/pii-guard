# PII Guard: Status

## Resume here
**M4 done (2026-10-10). Stopped for review.** Live demo: `.venv/bin/python -m pii.server` → **http://localhost:5240**
Engine (`pii/engine.py`) = rules + ONNX tagger (~9 ms) + format checks + conversation memory; API fail-closed, logs counts only.
Load: 30 msg/s steady → p95 19 ms, 0 errors; one process saturates ~70 msg/s.
Model results: see `reports/M3_REPORT.md` (leak 0.4–0.6% Ylemis, 2–5% Maskara). No retraining (Lan's call).
Next: M5 documents (PDF/photo → OCR → burned-in redaction) or M6 policies/vault/audit.

## M1 results: rule layer on synthetic data
| | Test (unseen templates) | Valid (seen templates) |
|---|---|---|
| Structured PII (13 rule labels) recall | **99.8%** | 98.9% |
| Structured PII precision | 100% | 100% |
| Names + addresses recall | **0%** (rules can't do these; that's the model's job) | 0% |
| All PII recall | **69.9%** | 54.8% |
| Latency per message | 0.03 ms mean, 0.07 ms p99 | 0.04 ms mean |

- The only rule misses are **spoken phone numbers** ("nine eight four…"), which are deliberate model-only cases.
- Full reports: `reports/m1_rules_test.md`, `reports/m1_rules_valid.md`.

## Caveats
- The rules score near-perfect partly because the generator uses formats the rules know. That's a circular test. The honest check is M2's **hand-written real-style set**.
- No OCR noise yet (that comes in M5); documents are clean text so far.

## Run it
```bash
cd ~/slm-lab/pii
python3 -m tests.test_rules                       # 7 tests
python3 -m pii.generate                           # data/train|valid|test.jsonl (9000/1000/1500)
python3 -m pii.evaluate data/test.jsonl           # recall/precision/latency report
python3 -m pii.redact "call me on 98450 12345, PAN ABCPK1234M"
```

## Files
- `pii/rules.py`: 13 detectors, checksums (Verhoeff, Luhn, GSTIN), context gates, overlap resolution
- `pii/redact.py`: consistent tokens + vault map
- `pii/fake.py`: fake-but-valid values + hard negatives
- `pii/generate.py`: 48 chat + 9 document templates (12 chat + 2 doc held out for test)
- `pii/evaluate.py`: per-label scoring
- `tests/test_rules.py`
