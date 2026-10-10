# PII Guard

India-first PII redaction for **customer chats and documents**: Aadhaar, PAN, GSTIN, UPI, Indian phone numbers, addresses with landmarks, Hinglish, and South Indian languages typed in English letters.

```
"hi mera order nahi aaya. Ramesh Kumar here, 98450 12345. upi refund to ramesh.k@okaxis pls"
                                      ↓  ~9 ms, CPU only
"hi mera order nahi aaya. [NAME_1] here, [PHONE_1]. upi refund to [UPI_1] pls"
```

![demo](reports/m4_demo.jpg)

## How it works
```
text ─► 1. Rules        regex + checksums (Verhoeff Aadhaar, Luhn card, GSTIN) + context words   (~0.1 ms)
     ─► 2. Tagger       fine-tuned DeBERTa-v3 token classifier, ONNX on CPU                       (~9 ms)
     ─► 3. Format checks relabel/drop implausible tagger output; whole words; follow "name is …"
     ─► 4. Memory       same person/number keeps the same token across a conversation
     ─► 5. Redact       token mode [NAME_1] (+ vault) or mask mode [NAME] (irreversible)
```
Rules win where they can verify (checksums); the model handles context (names, informal addresses, disguised numbers). The service **fails closed**: on any error it returns 503 and never echoes the input. Logs contain counts and timings, never text.

## Results
"Leak" = share of PII characters left readable after redaction (lower is better).

| Test set | Texts | Leak | Notes |
|---|---|---|---|
| [Ylemis India-PII benchmark](https://huggingface.co/datasets/Pranshurs/ylemis-india-pii-benchmark), Latin script | 5,945 | **0.6%** | independent, CC0 |
| Ylemis, native scripts (out of scope) | 4,055 | 0.4% | PII values mostly in Latin characters |
| [Maskara](https://huggingface.co/datasets/somukandula/maskara-indian-pii-200k) real-world eval | 2,600 | 2.1% | independent, MIT; many invalid synthetic IDs |
| Maskara template-disjoint eval | 10,457 | 4.6% | |
| Own hand-written set | 135 | 0.3% | optimistic (training data designed around its gaps) |

Compared on the hand-written set: rules + this tagger **0.3% @ 9 ms** · rules + Gemma-4 12B zero-shot 5.5% @ 3.5 s · rules + Gemma-4 E2B 7.5% @ 470 ms · rules + GLiNER-PII 14% @ 47 ms.

Load (one process, Apple M4 Pro): 30 msg/s steady → p95 19 ms, 0 errors; saturates around 70 msg/s.

Known weaknesses: false alarms on 20–33% of PII-free texts (tracking/order numbers, business names; errs toward over-masking); no labels yet for health IDs, account IDs, API keys/passwords; names written in Devanagari/Tamil script untested. Full write-ups: [`reports/M2_REPORT.md`](reports/M2_REPORT.md), [`reports/M3_REPORT.md`](reports/M3_REPORT.md).

## Model and licence
- **Code:** MIT (this repo).
- **Model weights are not in this repo.** The reference model was fine-tuned from [Piiranha](https://huggingface.co/iiiorg/piiranha-v1-detect-personal-information), which is **CC BY-NC-ND 4.0**, so it is kept in a **private** Hugging Face repo for personal, non-commercial use only.
- **To use PII Guard yourself, or commercially, train your own model** from the MIT-licensed `microsoft/deberta-v3-base` (or `mdeberta-v3-base` for multilingual):
  ```bash
  python -m pii.generate                                           # 15K synthetic examples, no real PII
  python -m pii.train --base microsoft/deberta-v3-base --out models/tagger-piiranha
  python -m pii.onnx_tagger export models/tagger-piiranha          # ONNX for serving
  ```

## Quick start (local demo)
```bash
python3.12 -m venv .venv && .venv/bin/pip install -r requirements-train.txt
python -m pii.generate && python -m pii.train --base microsoft/deberta-v3-base   # or put an existing model in models/tagger-piiranha
python -m pii.onnx_tagger export models/tagger-piiranha
.venv/bin/python -m pii.server                                  # http://localhost:5240 (demo mode)
```

## Docker
```bash
cp .env.example .env            # set PII_API_KEY; PII_MODEL_REPO + HF_TOKEN to download a private model
docker compose up --build       # http://localhost:5240/health
```
The image (~600 MB, no PyTorch) holds only code; the model is mounted at `/app/models/tagger` or downloaded at start-up from `PII_MODEL_REPO`. Defaults to `PII_MODE=prod` (no demo page, no vault endpoint).

| Env | Meaning |
|---|---|
| `PII_MODE` | `demo` (chat page + `/vault`) or `prod` |
| `PII_API_KEY` | if set, POST calls need `X-API-Key` |
| `PII_MODEL_DIR` / `PII_MODEL_REPO` / `HF_TOKEN` | where the model comes from |
| `PII_HOST` / `PII_PORT` | bind address (default `127.0.0.1:5240`, `0.0.0.0` in Docker) |

## API
```bash
curl -s localhost:5240/redact -H 'X-API-Key: …' \
  -d '{"text":"Ramesh 98450 12345","conversation_id":"chat-42","mode":"token"}'
# {"redacted":"[NAME_1] [PHONE_1]","entities":[{"label":"NAME","token":"[NAME_1]","start":0,"end":6,…}],"ms":9.4,…}
```
`POST /redact` · `POST /reset` · `GET /health` · `POST /vault` (demo mode only).

## Evaluate
```bash
python -m tests.test_rules                                   # rule unit tests
python -m pii.tagger models/tagger-piiranha data/handwritten.jsonl data/test.jsonl
scripts/fetch_external.sh && python -m pii.external          # independent benchmarks
python -m pii.onnx_tagger bench models/tagger-piiranha data/handwritten.jsonl
python -m pii.loadtest                                       # against a running server
```

## Layout
```
pii/rules.py         checksums, regexes, context gates          pii/engine.py     detection + memory + redaction
pii/tagger.py        tagger runtime + format checks             pii/server.py     HTTP service (fail closed)
pii/onnx_tagger.py   ONNX export/serving/bench                  pii/static/       demo chat page
pii/generate.py      synthetic data (templates + fake values)   pii/fake.py       fake-but-valid Indian IDs
pii/train.py         fine-tuning                                pii/evaluate.py   recall/precision/leak
pii/external.py      public benchmark scoring                   pii/baselines.py  GLiNER/Piiranha; pii/gemma.py Gemma
data/handwritten.txt hand-written test set ([[LABEL:value]])    PLAN.md · TASKS.md · STATUS.md
```

## DPDP note
PII Guard is a **security safeguard** (masking/tokenisation, as named in the DPDP Rules), not compliance by itself: consent, notices, rights requests and retention are separate obligations. Tokenised data is still personal data; only irreversible masking takes it out of scope. Not legal advice.
