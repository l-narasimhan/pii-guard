# Rule layer: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 8 | 100.0% | 0 | 100.0% |
| PAN | 5 | 4 | 80.0% | 0 | 100.0% |
| GSTIN | 5 | 5 | 100.0% | 0 | 100.0% |
| PHONE | 46 | 38 | 82.6% | 0 | 100.0% |
| EMAIL | 11 | 10 | 90.9% | 0 | 100.0% |
| UPI | 4 | 3 | 75.0% | 0 | 100.0% |
| CARD | 5 | 5 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 8 | 5 | 62.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 2 | 100.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 0 | 100.0% |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 2 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 96 | **87.3%** | 0 | **100.0%** |
| NAME | 77 | 0 | 0.0% | 0 | – |
| ADDRESS | 21 | 0 | 0.0% | 0 | – |
| DL | 1 | 1 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 209 | 97 | **46.4%** | 0 | |

**PII characters left visible (leak):** 59.1% overall; AADHAAR 0.0%, ADDRESS 100.0%, BANK_ACCT 36.6%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 11.2%, GSTIN 0.0%, IP 0.0%, NAME 100.0%, PAN 20.0%, PASSPORT 0.0%, PHONE 25.0%, UPI 28.4%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 78.8%, doc 94.8%

**Latency per message:** mean 0.024 ms · p95 0.057 ms · p99 0.082 ms

## Sample misses

- NAME: `priya` (handwritten)
- NAME: `Suresh Iyer` (handwritten)
- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- PHONE: `011 4567 8901` (handwritten)
- PHONE: `+971 50 123 4567` (handwritten)
- EMAIL: `ramesh dot kumar at gmail dot com` (handwritten)
- UPI: `sureshiyer@superyes` (handwritten)
- PAN: `AAKPV 4321 Q` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- ADDRESS: `No 14, 2nd cross, Gandhi Nagar, Hosur` (handwritten)
- ADDRESS: `Flat 1203 Tower B Lodha Palava Dombivli East` (handwritten)
- ADDRESS: `Sector 21, Plot 44, Kharghar, Navi Mumbai 410210` (handwritten)
- NAME: `Divya` (handwritten)
- NAME: `Rahul` (handwritten)
- NAME: `Lakshmi` (handwritten)
- NAME: `Shanti Devi` (handwritten)
- NAME: `Kiran Patil` (handwritten)
- NAME: `Karthik` (handwritten)
- NAME: `Manjunath` (handwritten)
- NAME: `Venkatesh Naidu` (handwritten)
- NAME: `Saraswathi` (handwritten)
- NAME: `Imran` (handwritten)
- NAME: `Sanjay` (handwritten)
- NAME: `Fatima Sheikh` (handwritten)
- PHONE: `nine eight four five zero one two three four five` (handwritten)
- NAME: `Meena Krishnan` (handwritten)
- NAME: `Joseph D'Souza` (handwritten)
- ADDRESS: `B-12 Rose Garden CHS, Bandra West` (handwritten)
- NAME: `Gurpreet` (handwritten)
- NAME: `Arjun` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Abdul Rahman` (handwritten)
- NAME: `Nandini` (handwritten)
- NAME: `Vikram Singh Rathore` (handwritten)
- ADDRESS: `H.No 8-2-293/82, Road No 14, Banjara Hills, Hyderabad 500034` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- ADDRESS: `4th floor, Prestige Tech Park, Marathahalli` (handwritten)

## Sample false alarms

- none
