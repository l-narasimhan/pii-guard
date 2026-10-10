# Rules + Piiranha: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 6 | 57.1% |
| PAN | 5 | 4 | 80.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 40 | 87.0% | 0 | 100.0% |
| EMAIL | 11 | 11 | 100.0% | 1 | 91.7% |
| UPI | 4 | 3 | 75.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 2 | 71.4% |
| BANK_ACCT | 8 | 6 | 75.0% | 4 | 60.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 100 | **90.9%** | 13 | **88.5%** |
| NAME | 77 | 61 | 79.2% | 4 | 93.8% |
| ADDRESS | 21 | 21 | 100.0% | 4 | 84.0% |
| DL | 1 | 1 | 100.0% | 2 | 33.3% |
| **All PII (incl. names/addresses)** | 209 | 183 | **87.6%** | 23 | |

**PII characters left visible (leak):** 17.8% overall; AADHAAR 0.0%, ADDRESS 29.6%, BANK_ACCT 21.5%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 21.3%, PAN 0.0%, PASSPORT 0.0%, PHONE 18.6%, UPI 28.4%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 86.5%, doc 94.8%

**Latency per message:** mean 29.666 ms · p95 40.978 ms · p99 44.958 ms

## Sample misses

- NAME: `priya` (handwritten)
- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `sureshiyer@superyes` (handwritten)
- PAN: `AAKPV 4321 Q` (handwritten)
- NAME: `Lakshmi` (handwritten)
- PHONE: `nine eight four five zero one two three four five` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Anita` (handwritten)
- NAME: `Shalini` (handwritten)
- NAME: `Imran Khan` (handwritten)
- NAME: `Ayesha` (handwritten)
- NAME: `John Peterson` (handwritten)
- PHONE: `nine eight one one zero four four three two one` (handwritten)
- NAME: `Arun Kumar` (handwritten)
- NAME: `Zainab Qureshi` (handwritten)
- NAME: `Teresa Fernandes` (handwritten)
- NAME: `Sanjay Kumar` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- NAME: `Imran Khan` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- NAME: `A. Banerjee` (handwritten)
- NAME: `S. Ghosh` (handwritten)
- NAME: `Ravi Kumar` (handwritten)
- NAME: `Ravi Kumar` (handwritten)

## Sample false alarms

- AADHAAR: ` 98450 1234O` (handwritten)
- AADHAAR: ` AAKPV 4321 Q` (handwritten)
- ADDRESS: ` Jayanagar` (handwritten)
- BANK_ACCT: ` 783420019812` (handwritten)
- BANK_ACCT: ` 9536 4556 8159` (handwritten)
- CARD: `198765012345678` (handwritten)
- ADDRESS: ` Whitefield` (handwritten)
- NAME: ` Ganesh Chaturthi` (handwritten)
- CARD: ` 403-1234567-7654321` (handwritten)
- AADHAAR: ` utr 412398765432` (handwritten)
- NAME: ` Hanuman Jayanti` (handwritten)
- DL: ` 8-2` (handwritten)
- AADHAAR: `-293/8` (handwritten)
- DL: `2` (handwritten)
- ADDRESS: ` Murugan` (handwritten)
- NAME: ` Mahalaxmi` (handwritten)
- BANK_ACCT: ` 004512` (handwritten)
- NAME: ` Murugan Stores` (handwritten)
- ADDRESS: ` Koramangala` (handwritten)
- BANK_ACCT: ` 783420019900` (handwritten)
- AADHAAR: ` 1120034455` (handwritten)
- AADHAAR: `123450987612345678` (handwritten)
- EMAIL: `customercare@shopkart.in` (handwritten)
