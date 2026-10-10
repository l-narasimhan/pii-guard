# PII Guard: Design & Plan

An India-first PII redaction agent for **customer chats and documents** (digital + scanned).
It runs as an internal service, redacts in milliseconds, and supports DPDP "reasonable security safeguards".

Task list with status: [TASKS.md](TASKS.md).

---

## 1. Goals

| Goal | Measure |
|---|---|
| Catch PII in chats and documents | Recall ≥ 98% overall; structured IDs (Aadhaar/PAN/card) 100% |
| Don't over-redact business data | Precision ≥ 90% |
| Fast enough to sit in the chat path | < 50 ms per chat message (p95) |
| Documents handled without user waiting | Digital ≤ 50 ms/page; scans ≤ 2 s/page, async |
| Never leaks by failure | Fail closed: if the service is down, nothing passes raw |
| Auditable | Every redaction stamped with model + policy version; no raw values in logs |

**Assumed volume** (no real numbers yet; mid-size Indian e-commerce/q-commerce):
~50K support chats/day × ~10 messages ≈ 5 lakh messages/day → ~6 msg/s average, **~25–30 msg/s peak**;
~5–10K document pages/day; ~1–2 lakh LLM-gateway calls/day. Used for latency and cost comparisons.

**Out of scope for now:** consent management, rights requests, other Indian scripts (Hindi in Devanagari, Kannada, etc.), audio.

---

## 2. Design

### 2.1 Components
```
            ┌──────────────────────── PII ENGINE ────────────────────────┐
 text ────► │ 1. Rule layer     regex + checksums/context  (~1 ms)       │
            │ 2. NER model      fine-tuned small encoder   (~10–20 ms)   │
            │ 3. Merge          union, longest span wins, conv. memory   │
            │ 4. Policy         per label: mask / token / keep / block   │
            └──────────────┬──────────────────────────────┬──────────────┘
                           ▼                              ▼
                    redacted text                  🔒 vault (token → value)

 documents: file → type detect → text+positions (direct or OCR) → ENGINE
            → burn-in boxes + flatten + strip metadata → redacted file
```

### 2.2 What counts as PII (labels)
| Label | Found by | Example |
|---|---|---|
| NAME | model | Ramesh Kumar, R. Iyer |
| ADDRESS | model | Flat B-104, Sobha Dream Acres, Whitefield 560066 |
| PHONE | rules + model (spoken/odd forms) | 98450 12345, +91-98450…, "nine eight four…" |
| EMAIL | rules | ramesh.k@gmail.com |
| UPI | rules | ramesh.k@okaxis, 9845012345@ybl |
| AADHAAR | rules (Verhoeff checksum) | 2345 6789 0124 |
| PAN | rules | ABCPK1234M |
| GSTIN | rules (checksum) | 29ABCPK1234M1Z5 |
| CARD | rules (Luhn) | 4111 1111 1111 1111 |
| BANK_ACCT | rules (needs "a/c"/"account" context) | a/c 50100123456789 |
| PASSPORT / VOTER_ID | rules (need context word) | passport M1234567 |
| VEHICLE | rules | KA 01 AB 1234 |
| DOB | rules (needs "dob"/"born" context) | DOB 14/03/1988 |
| IP | rules | 49.207.12.4 |

**Deliberately not PII** (hard negatives the model must learn to leave alone): order IDs, AWB/tracking numbers, SKUs, invoice numbers, amounts, a pincode on its own, IFSC codes, toll-free helplines, plain dates, shop names containing person names ("Ramesh Medicals", "Gupta & Sons"), festival and deity names ("Hanuman Jayanti sale").

### 2.3 Policies (same engine, different treatment)
| Policy | Used for | Behaviour |
|---|---|---|
| `support_chat` | Agent dashboard, chat storage | Tokenise everything, real values in vault |
| `llm_gateway` | Prompts to external AI | Tokenise, restore tokens in the reply if needed |
| `analytics` | Logs, BI, data lake | Irreversible mask (no vault entry), so the data is out of DPDP scope |
| `seller_kyc` | Seller documents | Keep GSTIN, redact PAN/Aadhaar/name/address |

### 2.4 Model choice
- **Small encoder NER** (DeBERTa/BERT-class, ~100–300M params), token classification with BIO tags.
- Why not a generative SLM: 5–10× slower, can rewrite or hallucinate text, and is bigger to serve.
- Trained on **synthetic data** (no real PII needed), tested on **unseen templates** + a small hand-written real-style set.
- Full fine-tune (the model is small) and LoRA compared side by side for learning.

### 2.5 Data design
- Generator builds text from **templates + fake-but-valid values** and records exact character spans, so labels are automatic and perfect.
- Chat style: English + Hinglish, lowercase, split/spoken numbers, call transcripts.
- Document style: KYC forms, invoices, PODs, complaint letters, seller/rider onboarding, export invoices, receipts, app logs.
- **Honest test:** some templates never appear in training; the test set uses only those.
- Format: JSONL `{"text", "spans":[{"start","end","label"}], "source", "template", "lang"}`.

### 2.6 Deployment (target)
- One Docker container (engine + model + policies), internal API `POST /redact`, India cloud region.
- Chats: synchronous call from the chat backend / webhook layer.
- LLM gateway: every AI call passes through it.
- Documents: quarantine bucket → queue → doc workers (OCR + engine) → redacted file released.
- Vault: encrypted Postgres, per-system access, reads logged, retention auto-delete.
- Fail closed, no raw logging, version stamps, monitoring, monthly retraining from reviewed misses.

---

## 3. Execution plan (milestones)

Each milestone ends with a **stop for review**.

| # | Milestone | Outcome | Where it runs |
|---|---|---|---|
| M1 | Rules + synthetic data | Rule layer, data generator, 11.5K labelled examples, rule-only baseline | Mac |
| M2 | Baselines | Rules vs an off-the-shelf model; know where the gaps are | Mac |
| M3 | Train the NER model | Fine-tuned model beating baseline; meets pass marks on test | Mac |
| M4 | Chat service + demo | Local API + chat page redacting live; latency measured | Mac (localhost) |
| M5 | Documents | Upload PDF/photo → OCR → redacted file download | Mac |
| M6 | Policies + vault + audit | Per-policy behaviour, token vault, restore, audit log, fail-closed | Mac |
| M7 | Package for deployment | Docker image, health checks, load test, deploy guide | Mac → cloud |
| M8 | Pilot | Real (masked) sample review, error loop, retrain | Company env |

---

## 4. Implementation notes
- Python 3.12, standard library for M1 (no installs). Later: `transformers`/`torch` (MPS) for training, ONNX Runtime for serving, a small HTTP server, an OCR engine for scans.
- Code layout:
```
pii/
  PLAN.md  TASKS.md
  pii/rules.py      rule layer (regex + checksums + context)
  pii/redact.py     spans → tokens, vault map
  pii/fake.py       fake values + hard negatives
  pii/generate.py   templates → labelled JSONL
  pii/evaluate.py   recall/precision/latency report
  tests/test_rules.py
  data/             train/valid/test JSONL (generated)
  reports/          evaluation outputs
```
