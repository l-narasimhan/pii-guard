# Rules + gemma-4-e2b-it-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 2 | 80.0% |
| PAN | 5 | 5 | 100.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 43 | 93.5% | 1 | 97.7% |
| EMAIL | 11 | 11 | 100.0% | 1 | 91.7% |
| UPI | 4 | 4 | 100.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 2 | 71.4% |
| BANK_ACCT | 8 | 6 | 75.0% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 105 | **95.5%** | 6 | **94.6%** |
| NAME | 77 | 72 | 93.5% | 2 | 97.3% |
| ADDRESS | 21 | 19 | 90.5% | 0 | 100.0% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 197 | **94.3%** | 8 | |

**PII characters left visible (leak):** 7.5% overall; AADHAAR 0.0%, ADDRESS 15.7%, BANK_ACCT 21.5%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 4.6%, PAN 0.0%, PASSPORT 0.0%, PHONE 8.2%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 96.2%, doc 94.8%

**Latency per message:** mean 0.036 ms · p95 0.084 ms · p99 0.121 ms

## Sample misses

- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- ADDRESS: `B-12 Rose Garden CHS, Bandra West` (handwritten)
- NAME: `Tanvi` (handwritten)
- NAME: `Shanti` (handwritten)
- NAME: `Ayesha` (handwritten)
- NAME: `John Peterson` (handwritten)
- PHONE: `nine eight one one zero four four three two one` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- NAME: `Mehul` (handwritten)

## Sample false alarms

- CARD: `99016` (handwritten)
- AADHAAR: `XXXX XXXX 4173` (handwritten)
- CARD: `7841` (handwritten)
- NAME: `ramu` (handwritten)
- PHONE: `1800 102 7777` (handwritten)
- NAME: `Murugan Stores` (handwritten)
- AADHAAR: `XXXX XXXX 8158` (handwritten)
- EMAIL: `customercare@shopkart.in` (handwritten)

Gemma stats: {"calls": 135, "returned": 183, "not_in_text": 1, "bad_json": 0, "bad_label": 1}
