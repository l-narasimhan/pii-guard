# gemma-4-e4b-it-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 4 | 50.0% | 0 | 100.0% |
| PAN | 5 | 3 | 60.0% | 0 | 100.0% |
| GSTIN | 5 | 0 | 0.0% | 0 | – |
| PHONE | 46 | 31 | 67.4% | 0 | 100.0% |
| EMAIL | 11 | 10 | 90.9% | 2 | 83.3% |
| UPI | 4 | 2 | 50.0% | 0 | 100.0% |
| CARD | 5 | 1 | 20.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 0 | 0.0% | 0 | – |
| PASSPORT | 2 | 0 | 0.0% | 0 | – |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 1 | 20.0% | 0 | 100.0% |
| DOB | 7 | 6 | 85.7% | 0 | 100.0% |
| IP | 2 | 1 | 50.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 61 | **55.5%** | 2 | **96.8%** |
| NAME | 77 | 55 | 71.4% | 0 | 100.0% |
| ADDRESS | 21 | 16 | 76.2% | 1 | 94.1% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 133 | **63.6%** | 3 | |

**PII characters left visible (leak):** 31.1% overall; AADHAAR 50.0%, ADDRESS 26.0%, BANK_ACCT 100.0%, CARD 81.4%, DL 0.0%, DOB 14.1%, EMAIL 11.2%, GSTIN 100.0%, IP 50.0%, NAME 22.3%, PAN 40.0%, PASSPORT 100.0%, PHONE 26.6%, UPI 0.0%, VEHICLE 80.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 51.9%, doc 58.6%

**Latency per message:** mean 804.625 ms · p95 2046.428 ms · p99 3152.113 ms

## Sample misses

- PHONE: `98450 77821` (handwritten)
- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- EMAIL: `ramesh dot kumar at gmail dot com` (handwritten)
- UPI: `9845012345@ybl` (handwritten)
- UPI: `kavya.r@okhdfcbank` (handwritten)
- AADHAAR: `9973 0911 4173` (handwritten)
- PAN: `bqrps7788l` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- BANK_ACCT: `39871234560` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- ADDRESS: `Flat 1203 Tower B Lodha Palava Dombivli East` (handwritten)
- NAME: `Karthik` (handwritten)
- NAME: `Saraswathi` (handwritten)
- NAME: `Imran` (handwritten)
- PHONE: `7019234412` (handwritten)
- VEHICLE: `KA51AB4321` (handwritten)
- VEHICLE: `MH 12 DE 4567` (handwritten)
- DOB: `3rd Jan 1992` (handwritten)
- PASSPORT: `M1234567` (handwritten)
- NAME: `Gurpreet` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Abdul Rahman` (handwritten)
- NAME: `Nandini` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- ADDRESS: `4th floor, Prestige Tech Park, Marathahalli` (handwritten)
- NAME: `Tanvi` (handwritten)
- PHONE: `9611234567` (handwritten)
- NAME: `Mohan` (handwritten)
- NAME: `Anita` (handwritten)
- NAME: `Shalini` (handwritten)
- PHONE: `7353112233` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- CARD: `8137929841622946` (handwritten)
- CARD: `6514-7513-6270-1074` (handwritten)
- BANK_ACCT: `004501234567` (handwritten)
- ADDRESS: `gali no 4, shiv mandir ke peeche, Laxmi Nagar` (handwritten)
- NAME: `Revathi` (handwritten)

## Sample false alarms

- ADDRESS: `delhi` (handwritten)
- EMAIL: `9845012345@ybl` (handwritten)
- EMAIL: `kavya.r@okhdfcbank` (handwritten)

Gemma stats: {"calls": 135, "returned": 136, "not_in_text": 1, "bad_json": 0, "bad_label": 0}
