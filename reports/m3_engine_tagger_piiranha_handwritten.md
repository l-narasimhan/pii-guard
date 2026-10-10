# Rules + tagger(tagger-piiranha): data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 0 | 100.0% |
| PAN | 5 | 5 | 100.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 44 | 95.7% | 0 | 100.0% |
| EMAIL | 11 | 11 | 100.0% | 0 | 100.0% |
| UPI | 4 | 4 | 100.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 8 | 100.0% | 1 | 88.9% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 1 | 87.5% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 108 | **98.2%** | 2 | **98.2%** |
| NAME | 77 | 77 | 100.0% | 3 | 96.2% |
| ADDRESS | 21 | 21 | 100.0% | 3 | 87.5% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 207 | **99.0%** | 8 | |

**PII characters left visible (leak):** 0.3% overall; AADHAAR 0.0%, ADDRESS 0.0%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 0.0%, PAN 0.0%, PASSPORT 0.0%, PHONE 1.9%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 96.2%, doc 100.0%

**Latency per message:** mean 27.307 ms · p95 35.585 ms · p99 39.685 ms

## Sample misses

- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)

## Sample false alarms

- ADDRESS: `delhi` (handwritten)
- NAME: `chaar` (handwritten)
- NAME: `usne` (handwritten)
- ADDRESS: `lane behind Murugan Stores` (handwritten)
- DOB: `1990` (handwritten)
- BANK_ACCT: `1120034455` (handwritten)
- ADDRESS: `10 min, 4 extra pickers per store, Bengaluru + Hyderabad` (handwritten)
- NAME: `Shree Krishna` (handwritten)
