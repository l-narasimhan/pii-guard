# Rules + gemma-4-12B-it-qat-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 0 | 100.0% |
| PAN | 5 | 5 | 100.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 44 | 95.7% | 2 | 95.7% |
| EMAIL | 11 | 11 | 100.0% | 0 | 100.0% |
| UPI | 4 | 4 | 100.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 5 | 62.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 105 | **95.5%** | 2 | **98.1%** |
| NAME | 77 | 75 | 97.4% | 1 | 98.7% |
| ADDRESS | 21 | 18 | 85.7% | 0 | 100.0% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 199 | **95.2%** | 3 | |

**PII characters left visible (leak):** 5.5% overall; AADHAAR 0.0%, ADDRESS 15.2%, BANK_ACCT 15.1%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 2.4%, PAN 0.0%, PASSPORT 0.0%, PHONE 1.9%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 94.2%, doc 96.6%

**Latency per message:** mean 0.030 ms · p95 0.073 ms · p99 0.172 ms

## Sample misses

- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- NAME: `Saraswathi` (handwritten)
- NAME: `Gurpreet` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- ADDRESS: `4th floor, Prestige Tech Park, Marathahalli` (handwritten)
- ADDRESS: `gali no 4, shiv mandir ke peeche, Laxmi Nagar` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)

## Sample false alarms

- NAME: `Ganesh` (handwritten)
- PHONE: `3011223344` (handwritten)
- PHONE: `3011223355` (handwritten)

Gemma stats: {"calls": 135, "returned": 190, "not_in_text": 0, "bad_json": 0, "bad_label": 0}
