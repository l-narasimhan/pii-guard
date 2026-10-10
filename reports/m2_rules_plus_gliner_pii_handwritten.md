# Rules + GLiNER-PII: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 2 | 80.0% |
| PAN | 5 | 5 | 100.0% | 2 | 71.4% |
| GSTIN | 5 | 5 | 100.0% | 1 | 83.3% |
| PHONE | 46 | 40 | 87.0% | 2 | 95.2% |
| EMAIL | 11 | 11 | 100.0% | 2 | 84.6% |
| UPI | 4 | 3 | 75.0% | 1 | 75.0% |
| CARD | 5 | 5 | 100.0% | 1 | 83.3% |
| BANK_ACCT | 8 | 5 | 62.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 1 | 83.3% |
| DOB | 7 | 7 | 100.0% | 1 | 87.5% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 100 | **90.9%** | 13 | **88.5%** |
| NAME | 77 | 59 | 76.6% | 15 | 79.7% |
| ADDRESS | 21 | 19 | 90.5% | 6 | 76.0% |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 179 | **85.6%** | 34 | |

**PII characters left visible (leak):** 14.0% overall; AADHAAR 0.0%, ADDRESS 14.7%, BANK_ACCT 36.6%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 21.1%, PAN 2.0%, PASSPORT 0.0%, PHONE 20.5%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 86.5%, doc 94.8%

**Latency per message:** mean 47.707 ms · p95 56.307 ms · p99 58.854 ms

## Sample misses

- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `sureshiyer@superyes` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- NAME: `Divya` (handwritten)
- NAME: `Imran` (handwritten)
- NAME: `Sanjay` (handwritten)
- PHONE: `nine eight four five zero one two three four five` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Abdul Rahman` (handwritten)
- NAME: `Vikram Singh Rathore` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- NAME: `Tanvi` (handwritten)
- NAME: `Shalini` (handwritten)
- PHONE: `nine eight one one zero four four three two one` (handwritten)
- NAME: `Ritu Arora` (handwritten)
- NAME: `Ramdas Pawar` (handwritten)
- NAME: `Arun Kumar` (handwritten)
- NAME: `Zainab Qureshi` (handwritten)
- NAME: `Teresa Fernandes` (handwritten)
- NAME: `Sanjay Kumar` (handwritten)
- BANK_ACCT: `3011223344` (handwritten)
- NAME: `Imran Khan` (handwritten)
- BANK_ACCT: `3011223355` (handwritten)
- NAME: `S. Ghosh` (handwritten)
- NAME: `Ravi Kumar` (handwritten)
- NAME: `Ravi Kumar` (handwritten)
- NAME: `Mehul` (handwritten)

## Sample false alarms

- UPI: `UPI` (handwritten)
- EMAIL: `sureshiyer@superyes` (handwritten)
- AADHAAR: `XXXX XXXX 4173` (handwritten)
- CARD: `7841` (handwritten)
- NAME: `I` (handwritten)
- ADDRESS: `address` (handwritten)
- ADDRESS: `parcel gate te chad deyo` (handwritten)
- PHONE: `1800 102 7777` (handwritten)
- NAME: `customer` (handwritten)
- ADDRESS: `Pincode 560078` (handwritten)
- GSTIN: `GST` (handwritten)
- NAME: `bhaiya gali no 4` (handwritten)
- ADDRESS: `lane behind Murugan Stores` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Customer` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Customer` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Customer` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `u_88213` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Agent` (handwritten)
- PHONE: `number` (handwritten)
- PAN: `PAN card copy` (handwritten)
- AADHAAR: `XXXX XXXX 8158` (handwritten)
- ADDRESS: `Address` (handwritten)
- PAN: `22` (handwritten)
- DOB: `1990` (handwritten)
- NAME: `______` (handwritten)
- ADDRESS: `address` (handwritten)
- VEHICLE: `KMC-44512` (handwritten)
- NAME: `Consumer` (handwritten)
- EMAIL: `customercare@shopkart.in` (handwritten)
