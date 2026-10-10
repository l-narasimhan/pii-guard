# M2 Report: Baselines (2026-10-10)

**Question:** before training our own model, how far do rules plus ready-made PII models get, and what's missing?

## Test sets
| Set | Size | What it is |
|---|---|---|
| **Hand-written** (`data/handwritten.txt`) | 135 items (97 chat, 38 doc), 209 PII spans, 24 with no PII | Written by hand, **not** from the generator: typos, Hinglish/Kannada/Tamil/Telugu in Latin script, letter-O-for-zero, split and spoken numbers, landlines, foreign numbers, "dot/at" emails, landmark-only addresses, names that are also ordinary words, CSV/WhatsApp exports, OCR-ish labels. **This is the honest set.** |
| Synthetic test | 1,500 | Generator output from templates never used in training |

## Headline: hand-written set
"Leak" = share of PII characters left visible, the number that matters for redaction.
"Found" = span-level recall (any overlap counts, so it's lenient).

| Detector | All PII found | **Leak** | False alarms | Speed (mean) |
|---|---|---|---|---|
| Rules only | 45.9% | 59.6% | 1 | 0.02 ms |
| GLiNER-PII alone | 74.6% | 20.3% | 40 | 48 ms |
| Piiranha alone | 57.9% | 36.0% | 39 | 29 ms |
| **Rules + GLiNER-PII** | 85.6% | **14.0%** | 34 | 47 ms |
| **Rules + Piiranha** | **87.6%** | 17.8% | **23** | **28 ms** |
| *Target (PLAN.md)* | *≥ 98%* | *≤ 2%* | | *< 20 ms model* |

On the synthetic test set, both combinations reach about 93.6% found, with 99.8% on structured IDs.

## What we learned
1. **Rules alone aren't enough on real text.** 99.8% on synthetic data became 87.3% on hand-written data for structured IDs. Synthetic data flatters the rules.
2. **Merge strategy matters.** Letting the longest span win let Piiranha's wrong long spans override checksum-verified Aadhaar matches (Aadhaar recall fell to 62.5%). The fix: **rule spans win; the model only fills gaps.** Now built in.
3. **"Found" overstates protection.** Piiranha "found" 100% of addresses but left 30% of address characters visible, because it tags only a city or street fragment. From now on we track the leak rate.
4. **Neither model knows India.** Piiranha catches 0% of PAN, GSTIN, UPI, vehicle and passport numbers; GLiNER is erratic on them. Rules cover these well.
5. **Speed:** both models run at 28–48 ms on CPU without optimisation, too slow for the < 20 ms model budget. ONNX + int8 (T3.8) is needed.
6. **Bug found and fixed:** the phone rule treated a newline as a number separator, which missed numbers at the end of lines in lists. Test added.

## Gaps our model must close (hand-written set)
| Gap | Examples | Who misses it |
|---|---|---|
| **Single first names** in greetings, thanks, relations | "Thanks Divya", "Tanvi ka number", "Anita madam", "Hi Mehul" | both models |
| **Names in tables and lists** | CSV rows, payout sheets, manifests, WhatsApp exports | both models |
| **Unstructured addresses** | "3rd house after ramu tea stall, blue gate…", "gali no 4, shiv mandir ke peeche…" | GLiNER; Piiranha only partial |
| **Obfuscated numbers** | `98450 1234O`, split `99016 … 44328`, spoken digits, glued `mob9845…` | everything |
| **Landline and foreign numbers** | `011 4567 8901`, `+971 50 123 4567` | rules; partly models |
| **Bank numbers without a keyword** | `send to 50100234567812 hdfc`, payout sheet rows | rules; partly models |
| **Odd formats** | spaced PAN `AAKPV 4321 Q`, unknown UPI handle `@superyes`, "dot/at" emails | rules |
| **Driving licence** | `KA0520190012345` | rules (no detector yet) |

## False alarms to train away
- **Speaker labels and common words** tagged as names: "Agent", "Customer", "haan ji", "I", "bhaiya".
- **Business, festival and deity names:** "Murugan Stores", "Ganesh Chaturthi", "Hanuman Jayanti", "Mahalaxmi".
- **A locality alone** treated as an address: "Whitefield", "Koramangala", "Pincode 560078".
- **Masked IDs and company data:** `XXXX XXXX 4173`, `card ending 7841`, the toll-free `1800…` number, `customercare@company` inboxes.
- **Long order, AWB and UTR numbers** taken as card, bank or Aadhaar numbers by Piiranha.

## Decision for M3
- **Engine = rules first + our own fine-tuned token classifier**, merged with rules winning.
- **Base model:** start from **Piiranha's DeBERTa-v3 backbone**, which already knows PII and is fastest here. Replace its output layer with our 16 labels and fine-tune on our data. Compare against plain `deberta-v3-base` and multilingual `mdeberta-v3-base` (the latter matters for future Indian scripts).
- **Improve the generator first** (new tasks T3.0.x) so the training data covers the gaps above. Every gap row becomes templates or value variants, and every false-alarm row becomes hard negatives.
- **Guard against overfitting to my writing style:** the hand-written set stays test-only and never feeds the generator's exact sentences. A second hand-written set (ideally your real masked samples) is the final exam.
