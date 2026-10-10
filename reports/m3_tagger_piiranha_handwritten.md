# tagger(tagger-piiranha): data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 5 | 62.5% | 0 | 100.0% |
| PAN | 5 | 5 | 100.0% | 1 | 83.3% |
| GSTIN | 5 | 4 | 80.0% | 0 | 100.0% |
| PHONE | 46 | 44 | 95.7% | 10 | 81.5% |
| EMAIL | 11 | 10 | 90.9% | 0 | 100.0% |
| UPI | 4 | 4 | 100.0% | 2 | 66.7% |
| CARD | 5 | 4 | 80.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 8 | 100.0% | 2 | 80.0% |
| PASSPORT | 2 | 1 | 50.0% | 0 | 100.0% |
| VOTER_ID | 2 | 1 | 50.0% | 2 | 33.3% |
| VEHICLE | 5 | 5 | 100.0% | 1 | 83.3% |
| DOB | 7 | 7 | 100.0% | 1 | 87.5% |
| IP | 2 | 1 | 50.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 99 | **90.0%** | 19 | **83.9%** |
| NAME | 77 | 77 | 100.0% | 3 | 96.2% |
| ADDRESS | 21 | 21 | 100.0% | 3 | 87.5% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 198 | **94.7%** | 25 | |

**PII characters left visible (leak):** 1.9% overall; AADHAAR 0.0%, ADDRESS 0.0%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 13.2%, GSTIN 0.0%, IP 0.0%, NAME 0.0%, PAN 0.0%, PASSPORT 0.0%, PHONE 2.8%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 50.0%

**Rule-label recall by source:** chat 84.6%, doc 94.8%

**Latency per message:** mean 27.412 ms · p95 36.543 ms · p99 54.298 ms

## Sample misses

- PHONE: `44328` (handwritten)
- AADHAAR: `9973 0911 4173` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- PASSPORT: `M1234567` (handwritten)
- IP: `49.207.12.4` (handwritten)
- PHONE: `9611234567` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- CARD: `8137929841622946` (handwritten)
- VOTER_ID: `ABX5512309` (handwritten)
- EMAIL: `anil.menon@krishnadairy.in` (handwritten)
- AADHAAR: `8488 7663 4407` (handwritten)

## Sample false alarms

- PHONE: `ph` (handwritten)
- ADDRESS: `delhi` (handwritten)
- PHONE: `-` (handwritten)
- PHONE: `97` (handwritten)
- PHONE: `9973 0911 4173` (handwritten)
- PAN: `10AAKPV4321Q8Z7` (handwritten)
- PHONE: `9536 4556 8159` (handwritten)
- PHONE: `560066` (handwritten)
- VEHICLE: `M1234567` (handwritten)
- PHONE: `49.207.12.4` (handwritten)
- NAME: `chaar` (handwritten)
- PHONE: `78` (handwritten)
- NAME: `usne` (handwritten)
- VOTER_ID: `CUST-88213` (handwritten)
- PHONE: `6472 9405 5765` (handwritten)
- BANK_ACCT: `8137929841622946` (handwritten)
- ADDRESS: `lane behind Murugan Stores` (handwritten)
- UPI: `anil.menon@` (handwritten)
- VOTER_ID: `EMP-2231` (handwritten)
- DOB: `1990` (handwritten)
- UPI: `hil@` (handwritten)
- BANK_ACCT: `1120034455` (handwritten)
- ADDRESS: `10 min, 4 extra pickers per store, Bengaluru + Hyderabad` (handwritten)
- NAME: `Shree Krishna` (handwritten)
- PHONE: `8488 7663 4407` (handwritten)
