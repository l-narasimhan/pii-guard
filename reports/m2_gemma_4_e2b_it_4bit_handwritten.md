# gemma-4-e2b-it-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 5 | 62.5% | 2 | 71.4% |
| PAN | 5 | 5 | 100.0% | 1 | 83.3% |
| GSTIN | 5 | 2 | 40.0% | 0 | 100.0% |
| PHONE | 46 | 32 | 69.6% | 3 | 91.4% |
| EMAIL | 11 | 10 | 90.9% | 1 | 90.9% |
| UPI | 4 | 3 | 75.0% | 0 | 100.0% |
| CARD | 5 | 4 | 80.0% | 2 | 66.7% |
| BANK_ACCT | 8 | 4 | 50.0% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 1 | 50.0% | 0 | 100.0% |
| VEHICLE | 5 | 3 | 60.0% | 0 | 100.0% |
| DOB | 7 | 6 | 85.7% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 79 | **71.8%** | 9 | **89.8%** |
| NAME | 77 | 72 | 93.5% | 3 | 96.0% |
| ADDRESS | 21 | 19 | 90.5% | 0 | 100.0% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 171 | **81.8%** | 12 | |

**PII characters left visible (leak):** 15.3% overall; AADHAAR 26.0%, ADDRESS 15.7%, BANK_ACCT 45.2%, CARD 0.0%, DL 0.0%, DOB 14.1%, EMAIL 0.0%, GSTIN 46.7%, IP 0.0%, NAME 4.6%, PAN 0.0%, PASSPORT 0.0%, PHONE 29.0%, UPI 0.0%, VEHICLE 40.0%, VOTER_ID 50.0%

**Rule-label recall by source:** chat 76.9%, doc 67.2%

**Latency per message:** mean 472.172 ms · p95 1146.165 ms · p99 1720.954 ms

## Sample misses

- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `kavya.r@okhdfcbank` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- PHONE: `9741203345` (handwritten)
- PHONE: `7019234412` (handwritten)
- ADDRESS: `B-12 Rose Garden CHS, Bandra West` (handwritten)
- PHONE: `9663301122` (handwritten)
- NAME: `Tanvi` (handwritten)
- PHONE: `7353112233` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- CARD: `8137929841622946` (handwritten)
- BANK_ACCT: `004501234567` (handwritten)
- PHONE: `94480 55123` (handwritten)
- PHONE: `7019988776` (handwritten)
- DOB: `12-07-1979` (handwritten)
- GSTIN: `24CXZPM1029K4ZW` (handwritten)
- NAME: `Shanti` (handwritten)
- GSTIN: `34BQRPS7788L8ZC` (handwritten)
- PHONE: `9444012345` (handwritten)
- VEHICLE: `TS09EK4321` (handwritten)
- VOTER_ID: `ABX5512309` (handwritten)
- NAME: `Ayesha` (handwritten)
- PHONE: `9845098450` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- NAME: `John Peterson` (handwritten)
- PHONE: `nine eight one one zero four four three two one` (handwritten)
- VEHICLE: `MH 04 GH 1122` (handwritten)
- PHONE: `9821001234` (handwritten)
- PHONE: `9900112233` (handwritten)
- AADHAAR: `8978-8093-2083` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- PHONE: `9845076543` (handwritten)
- BANK_ACCT: `6012345678` (handwritten)
- EMAIL: `mehul.shah@gmail.com` (handwritten)
- NAME: `Mehul` (handwritten)
- AADHAAR: `8488 7663 4407` (handwritten)

## Sample false alarms

- CARD: `99016` (handwritten)
- EMAIL: `kavya.r@okhdfcbank` (handwritten)
- AADHAAR: `XXXX XXXX 4173` (handwritten)
- CARD: `7841` (handwritten)
- NAME: `ramu` (handwritten)
- PHONE: `1800 102 7777` (handwritten)
- PHONE: `6472 9405 5765` (handwritten)
- PHONE: `8137929841622946` (handwritten)
- NAME: `Murugan Stores` (handwritten)
- PAN: `BQRPS7788L` (handwritten)
- AADHAAR: `XXXX XXXX 8158` (handwritten)
- NAME: `mehul.shah@gmail.com` (handwritten)

Gemma stats: {"calls": 135, "returned": 183, "not_in_text": 1, "bad_json": 0, "bad_label": 1}
