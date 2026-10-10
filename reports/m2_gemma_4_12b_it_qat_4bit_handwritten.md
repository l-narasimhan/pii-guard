# gemma-4-12B-it-qat-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 6 | 75.0% | 0 | 100.0% |
| PAN | 5 | 5 | 100.0% | 1 | 83.3% |
| GSTIN | 5 | 0 | 0.0% | 0 | – |
| PHONE | 46 | 44 | 95.7% | 3 | 93.6% |
| EMAIL | 11 | 11 | 100.0% | 1 | 91.7% |
| UPI | 4 | 3 | 75.0% | 0 | 100.0% |
| CARD | 5 | 4 | 80.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 3 | 37.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 4 | 80.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 0 | 0.0% | 0 | – |
| **Rule labels total** | 110 | 91 | **82.7%** | 5 | **94.8%** |
| NAME | 77 | 75 | 97.4% | 1 | 98.7% |
| ADDRESS | 21 | 18 | 85.7% | 0 | 100.0% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 185 | **88.5%** | 6 | |

**PII characters left visible (leak):** 10.4% overall; AADHAAR 12.0%, ADDRESS 15.2%, BANK_ACCT 38.7%, CARD 18.6%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 86.7%, IP 100.0%, NAME 2.4%, PAN 0.0%, PASSPORT 0.0%, PHONE 1.9%, UPI 0.0%, VEHICLE 20.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 80.8%, doc 84.5%

**Latency per message:** mean 3532.512 ms · p95 7127.326 ms · p99 10564.727 ms

## Sample misses

- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `kavya.r@okhdfcbank` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- NAME: `Saraswathi` (handwritten)
- VEHICLE: `KA51AB4321` (handwritten)
- IP: `49.207.12.4` (handwritten)
- NAME: `Gurpreet` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- ADDRESS: `4th floor, Prestige Tech Park, Marathahalli` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- CARD: `8137929841622946` (handwritten)
- BANK_ACCT: `004501234567` (handwritten)
- ADDRESS: `gali no 4, shiv mandir ke peeche, Laxmi Nagar` (handwritten)
- GSTIN: `24CXZPM1029K4ZW` (handwritten)
- GSTIN: `34BQRPS7788L8ZC` (handwritten)
- IP: `103.21.44.9` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- GSTIN: `24CXZPM1029K4ZW` (handwritten)
- BANK_ACCT: `6012345678` (handwritten)
- AADHAAR: `8488 7663 4407` (handwritten)

## Sample false alarms

- EMAIL: `kavya.r@okhdfcbank` (handwritten)
- NAME: `Ganesh` (handwritten)
- PAN: `BQRPS7788L` (handwritten)
- PHONE: `3011223344` (handwritten)
- PHONE: `3011223355` (handwritten)
- PHONE: `8488 7663 4407` (handwritten)

Gemma stats: {"calls": 135, "returned": 190, "not_in_text": 0, "bad_json": 0, "bad_label": 0}
