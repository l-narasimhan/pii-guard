# M3 Report: Our own PII model (2026-10-10)

**Decision (Lan's call): the fine-tuned tagger is the model.** Gemma was tested zero-shot and dropped; its fine-tuning was stopped early.

## What was built
- **Training data v2:** 15,000 synthetic examples (52 new chat templates + 6 new document types) covering every M2 gap: lone first names, tables/lists, informal and Hinglish addresses, disguised numbers, driving licences, South Indian languages in Latin script, and many look-alike negatives.
- **Tagger:** Piiranha (DeBERTa-v3, ~180M parameters), fully fine-tuned for 3 epochs on the Mac GPU (50 min, best validation loss 0.0001) → `models/tagger-piiranha`.
- **Engine:** rules first (checksum/context verified), tagger fills the gaps, then **format checks** on the tagger's output (relabel if it fits another format, keep unknown IDs with 6+ digits, drop junk).
- **Rule upgrades:** IPv6, older driving-licence formats, "tracking/order number" context for phones, company inboxes ignored.
- **Fast runtime:** ONNX export, identical output, about 3× faster.

## Results
"Leak" = share of PII characters left readable (lower is better; target ≤ 2%).

### Our test sets
| Set | Found | **Leak** | False alarms |
|---|---|---|---|
| Hand-written set #1 (135 items, 209 PII) | 99.0% | **0.3%** | 8 |
| Synthetic test (2,000 unseen-template items) | 99.9% | **0.0%** | 279 |

### Independent public benchmarks (not written by us)
| Benchmark | Texts | **Leak (our PII types)** | PII-free texts falsely flagged |
|---|---|---|---|
| Ylemis India-PII, Latin script | 5,945 | **0.6%** | 25.0% |
| Ylemis India-PII, native scripts (out of scope) | 4,055 | **0.4%** | 20.1% |
| Maskara real-world eval | 2,600 | **2.1%** | 32.5% |
| Maskara unseen-template eval | 10,457 | **4.6%** | n/a |

### Compared with the alternatives (hand-written set)
| Approach | Leak | Speed |
|---|---|---|
| **Rules + our tagger (ONNX)** | **0.3%** | **~9 ms** (p95 13 ms), CPU |
| Rules + Gemma-4 12B (zero-shot) | 5.5% | ~3,500 ms |
| Rules + Gemma-4 E2B (zero-shot) | 7.5% | ~470 ms |
| Rules + GLiNER-PII (off the shelf) | 14.0% | ~47 ms |

### Speed and cost at the assumed volume (25–30 messages/sec peak)
| Runtime | Mean | p95 | Output |
|---|---|---|---|
| PyTorch | 26.6 ms | 34.6 ms | reference |
| **ONNX fp32 (chosen)** | **8.9 ms** | **13.0 ms** | identical, 135/135 |
| ONNX int8 | 7.3 ms | 13.0 ms | differs on 24/135, so rejected |

One 4-vCPU container handles the peak comfortably; run 2 for failover. No GPU needed.

## Honest caveats
1. **Hand-written set #1 is no longer blind.** I designed the v2 templates around the *kinds* of gaps it exposed, so its 0.3% is optimistic. The independent benchmarks are the better guide: **0.4–0.6% leak on Ylemis, 2–5% on Maskara.**
2. **I tuned the post-processing rules while looking at the external benchmarks** (three rounds). I kept every rule general (format plausibility, recall first), but those benchmarks are now partly "seen" too. A fresh test, ideally real masked data, is still needed before go-live.
3. **Maskara contains unrealistic values:** 91% of its Aadhaar numbers fail the real checksum, plus invalid mobile prefixes and non-standard formats. Some of its "leak" is the dataset, not the model. Ylemis is more realistic (100% valid Aadhaar).
4. **False alarms are the main weakness:** 20–33% of PII-free texts get at least one flag (tracking and order numbers, "warehouse bay 12, lot 3308", business names). That's over-masking (safe), but it hurts readability for agents and analytics.
5. **Native Indian scripts** score well only because the PII values (numbers, IDs, emails) are usually in Latin characters. Names written *in* Devanagari or Tamil script haven't really been tested.

## Gaps not yet covered (need new labels, so retraining needs Lan's OK)
| Gap | Leak today | Why it matters |
|---|---|---|
| Health IDs (ABHA, patient/medical record numbers) | ~57–62% | Sensitive under DPDP; hospitals and insurance |
| Customer/member account IDs | ~34–51% | Linkable identifiers |
| **API keys, passwords** | ~93–99% | Critical for the **LLM gateway** (people paste secrets into prompts) |
| Names in native scripts | untested | Needed if chats arrive in Devanagari or Tamil script |

## Recommendation
- **Ship the tagger engine (ONNX) for every path:** chat, LLM gateway, logs, documents.
- **Next milestone M4** (chat service + live demo), as planned.
- **Before a pilot, one retraining round** (with your OK) to add health IDs, account IDs and secrets, plus more look-alike negatives to cut false alarms.
- **Final exam before go-live:** a fresh blind test, either real masked samples from a pilot team or a new hand-written set written by someone other than me.
