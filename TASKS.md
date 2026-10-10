# PII Guard: Tasks

Small tasks, one milestone at a time; each milestone stops for review. Design: [PLAN.md](PLAN.md).
Status: `[x]` done · `[ ]` todo · `[~]` in progress

## M1: Rules + synthetic data
- [x] T1.1 Project skeleton (`pii/`, `tests/`, `data/`, `reports/`)
- [x] T1.2 Checksums: Verhoeff (Aadhaar), Luhn (card), GSTIN check char
- [x] T1.3 Rule detectors: Aadhaar, PAN, GSTIN, phone, email, UPI, card, vehicle, IP
- [x] T1.4 Context-gated detectors: bank a/c, passport, voter ID, DOB
- [x] T1.5 Hard-negative guards: AWB/order/UTR numbers not taken as Aadhaar; no matches inside longer IDs
- [x] T1.6 Overlap resolution (longest span, then priority)
- [x] T1.7 Redactor: consistent tokens (`[NAME_1]`), vault map, CLI
- [x] T1.8 Fake value generators (valid checksums) + hard negatives
- [x] T1.9 Chat templates: English, Hinglish, call transcripts
- [x] T1.10 Document templates: KYC, invoice, POD, complaint, seller/rider onboarding, export, receipt, logs
- [x] T1.11 Generator: spans recorded automatically; held-out templates for test; JSONL out
- [x] T1.12 Unit tests for rules + redactor
- [x] T1.13 Evaluator: per-label recall/precision, latency, sample misses
- [x] T1.14 Run: generate data, run tests, rule-only baseline report
- [x] T1.15 STATUS.md + review stop

## M2: Baselines
- [x] T2.1 Hand-written real-style test set: 135 items, 209 spans (`data/handwritten.txt`, `[[LABEL:value]]` markup)
- [x] T2.2 Rule baseline on hand-written set (87.3% structured, 45.9% all PII)
- [x] T2.3 Off-the-shelf models: GLiNER-PII, Piiranha (venv `.venv`)
- [x] T2.4 Combined rules + model (rules win on overlap); gap analysis; char-level leak metric added
- [x] T2.5 Report (`reports/M2_REPORT.md`) + review stop
- [x] (bugfix) Phone rule treated newline as separator; fixed + test

## M3: Train the NER model
Data first (from M2 gaps):
- [x] T3.0.1 Single-first-name templates (greetings, thanks, relations, "X madam/ji/sir")
- [x] T3.0.2 Table/list docs: CSV exports, payout sheets, manifests, WhatsApp exports, email signatures
- [x] T3.0.3 Unstructured/landmark addresses (English + Hinglish + "gali/mandir/peeche"); more ADDRESS overall
- [x] T3.0.4 Obfuscated values: O-for-0, split numbers, glued text, landlines, +971/+1/+44 numbers, "dot/at" emails, spaced PAN, unknown UPI handles, bank numbers without keyword
- [x] T3.0.5 Hard negatives: speaker labels, masked IDs, "card ending 1234", localities alone, company inboxes, festival/deity/business names
- [x] T3.0.6 Driving licence: rule + generator + label `DL`
- [x] T3.0.7 South Indian languages in Latin script (Kannada/Tamil/Telugu/Malayalam) templates
Training (two tracks, trained one after the other; ask Lan before any training run):
- [x] T3.1 Install `transformers`/`torch` (MPS) + `mlx-lm`; bases: Piiranha (tagger), Gemma-4 E2B (generative)
- [x] T3.2 Convert char spans → BIO tags; alignment check (100% synthetic, 208/209 hand-written)
- [x] T3.3 Training script + inference/engine wrapper; CPU smoke test passes end to end
- [x] T3.3b Gemma zero-shot baselines: E2B 7.5% leak (best), E4B 15.6%, 12B (running)
- [x] T3.3c Gemma SFT data: compact JSON answers, short instruction (`data/sft/`)
- [x] T3.4 Track A: tagger trained (Piiranha base, 3 epochs, 50 min, best valid loss 0.0001) → `models/tagger-piiranha`. Engine on hand-written: 99.5% found, **0.2% leak**, 14 false alarms, ~27 ms CPU
- [-] T3.5 Track B: Gemma-4 E2B LoRA, **stopped by Lan** (tagger already beats all Gemma variants; LoRA would take ~2 h)
- [x] T3.6 Compare: tagger engine 0.2% leak @27 ms vs Rules+Gemma 12B 5.5% @3.5 s, E2B 7.5% @0.47 s, GLiNER 14% @47 ms
- [x] T3.7 Error review + independent benchmarks (Ylemis 10K, Maskara 13K) instead of set #2; format post-filter + rule upgrades (IPv6, old DL formats, phone context); no retraining
- [x] T3.8 Speed: ONNX fp32 = identical output, 8.9 ms mean / 13 ms p95 (PyTorch 26.6 ms); int8 rejected (changes 24/135 outputs)
- [x] T3.9 Report `reports/M3_REPORT.md` + review stop
- [ ] T3.10 (needs Lan's OK) retrain round: health IDs, account IDs, API keys/passwords, more negatives to cut false alarms

## M4: Chat service + demo
- [x] T4.1 Engine (`pii/engine.py`): rules + ONNX tagger + format checks + conversation memory (same value/name → same token across messages); token vs mask mode
- [x] T4.2 Local API (`pii/server.py`, port 5240): POST /redact, /vault (demo), /reset; GET /health; fail-closed; logs counts only
- [x] T4.3 Chat demo (`pii/static/chat.html`): customer vs agent view, live preview, samples, vault panel; verified in Chrome (`reports/m4_demo.jpg`)
- [x] T4.4 Load test (`reports/m4_loadtest.md`): 30 msg/s steady → p95 19 ms, 0 errors; saturates ~70 msg/s per process
- [x] T4.5 Review stop

## M5: Documents
- [ ] T5.1 Digital PDF/DOCX text + word positions extraction
- [ ] T5.2 OCR for scans/photos (word boxes)
- [ ] T5.3 Map engine spans → page boxes
- [ ] T5.4 Burn-in redaction + flatten + strip metadata
- [ ] T5.5 ID-card region detection (Aadhaar/PAN card images)
- [ ] T5.6 Synthetic scanned test docs; measure recall after OCR
- [ ] T5.7 Upload/download demo page
- [ ] T5.8 Review stop

## M6: Policies, vault, audit
- [ ] T6.1 Policy file (YAML/JSON) per use: support_chat, llm_gateway, analytics, seller_kyc
- [ ] T6.2 Vault: encrypted store, token → value, per-caller access
- [ ] T6.3 Restore endpoint (for authorised systems only)
- [ ] T6.4 Audit log: counts/labels/policy/model version, no raw values
- [ ] T6.5 Fail-closed behaviour + tests
- [ ] T6.6 Review stop

## M7: Package for deployment
- [x] T7.1 Dockerfile (621 MB, no PyTorch); model mounted or downloaded from private HF repo (not baked in: licence + size)
- [x] T7.2 Config via env (PII_MODE demo|prod, PII_API_KEY, PII_HOST/PORT, PII_MODEL_*); /health + Docker HEALTHCHECK; warm-up
- [x] T7.2b Repo: README, MIT licence (code), requirements-serve/train, docker-compose, .env.example, fetch/upload scripts
- [x] T7.2c Code pushed to public GitHub l-narasimhan/pii-guard
- [x] T7.2d Model → private HF lan1983/pii-guard-tagger (verified private; container downloads it with HF_TOKEN in ~1 min, serves correctly)
- [x] T7.2e README "Using it with someone else's chat app" + `examples/webhook_relay.py` (signature check, fail closed; tested)
- [ ] T7.3 Doc worker + queue setup (local equivalent)
- [ ] T7.4 Load test; sizing guide
- [ ] T7.5 Deployment guide (India region, network, vault, monitoring)
- [ ] T7.6 Review stop

## M7b: Platform connectors (proposed, not started)
- [ ] Multi-tenant API keys + per-customer settings (needs M6 policies)
- [ ] Freshchat app (Freshworks serverless, onMessageCreate): detect + flag + agent warning + redacted copy downstream (customer replies can't be edited via API)
- [ ] Google Chat app (Workspace Events message.created): warn; admin-mode delete + re-post redacted copy; DLP custom-detector pack
- [ ] No-code webhook connector per tenant (examples/webhook_relay.py hardened)

## M8: Pilot
- [ ] T8.1 Pick one channel (e.g. support chat) + one doc type
- [ ] T8.2 Shadow mode: redact in parallel, nothing blocked; humans review a sample
- [ ] T8.3 Misses → new training examples → retrain
- [ ] T8.4 Go-live criteria check against PLAN goals
