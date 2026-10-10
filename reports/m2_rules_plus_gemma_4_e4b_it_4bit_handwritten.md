# Rules + gemma-4-e4b-it-4bit: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 0 | 100.0% |
| PAN | 5 | 5 | 100.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 42 | 91.3% | 0 | 100.0% |
| EMAIL | 11 | 10 | 90.9% | 1 | 90.9% |
| UPI | 4 | 4 | 100.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 5 | 62.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 102 | **92.7%** | 1 | **99.0%** |
| NAME | 77 | 55 | 71.4% | 0 | 100.0% |
| ADDRESS | 21 | 16 | 76.2% | 1 | 94.1% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 174 | **83.3%** | 2 | |

**PII characters left visible (leak):** 15.6% overall; AADHAAR 0.0%, ADDRESS 26.0%, BANK_ACCT 36.6%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 11.2%, GSTIN 0.0%, IP 0.0%, NAME 22.3%, PAN 0.0%, PASSPORT 0.0%, PHONE 5.7%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 88.5%, doc 96.6%

**Latency per message:** mean 0.024 ms · p95 0.055 ms · p99 0.080 ms

## Sample misses

- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- EMAIL: `ramesh dot kumar at gmail dot com` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- ADDRESS: `Flat 1203 Tower B Lodha Palava Dombivli East` (handwritten)
- NAME: `Karthik` (handwritten)
- NAME: `Saraswathi` (handwritten)
- NAME: `Imran` (handwritten)
- NAME: `Gurpreet` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Abdul Rahman` (handwritten)
- NAME: `Nandini` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- ADDRESS: `4th floor, Prestige Tech Park, Marathahalli` (handwritten)
- NAME: `Tanvi` (handwritten)
- NAME: `Mohan` (handwritten)
- NAME: `Anita` (handwritten)
- NAME: `Shalini` (handwritten)
- ADDRESS: `gali no 4, shiv mandir ke peeche, Laxmi Nagar` (handwritten)
- NAME: `Revathi` (handwritten)
- NAME: `K. Iyer` (handwritten)
- NAME: `Ayesha` (handwritten)
- NAME: `Pooja` (handwritten)
- NAME: `Harjeet Singh Gill` (handwritten)
- NAME: `Sanjay Kumar` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- NAME: `Imran Khan` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- NAME: `Ishaan` (handwritten)
- NAME: `Kunal` (handwritten)
- NAME: `Ravi Kumar` (handwritten)
- NAME: `Ravi Kumar` (handwritten)
- NAME: `Mehul` (handwritten)

## Sample false alarms

- ADDRESS: `delhi` (handwritten)
- EMAIL: `customercare@shopkart.in` (handwritten)

Gemma stats: {"calls": 135, "returned": 136, "not_in_text": 1, "bad_json": 0, "bad_label": 0}
