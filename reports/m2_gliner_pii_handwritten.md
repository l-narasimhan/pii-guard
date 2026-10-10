# GLiNER-PII: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 6 | 75.0% | 3 | 66.7% |
| PAN | 5 | 5 | 100.0% | 2 | 71.4% |
| GSTIN | 5 | 5 | 100.0% | 1 | 83.3% |
| PHONE | 46 | 25 | 54.3% | 3 | 89.3% |
| EMAIL | 11 | 11 | 100.0% | 4 | 73.3% |
| UPI | 4 | 0 | 0.0% | 1 | 0.0% |
| CARD | 5 | 4 | 80.0% | 1 | 80.0% |
| BANK_ACCT | 8 | 5 | 62.5% | 0 | 100.0% |
| PASSPORT | 2 | 2 | 100.0% | 0 | 100.0% |
| VOTER_ID | 2 | 1 | 50.0% | 0 | 100.0% |
| VEHICLE | 5 | 5 | 100.0% | 2 | 71.4% |
| DOB | 7 | 7 | 100.0% | 1 | 87.5% |
| IP | 2 | 1 | 50.0% | 0 | 100.0% |
| **Rule labels total** | 110 | 77 | **70.0%** | 18 | **81.1%** |
| NAME | 77 | 59 | 76.6% | 15 | 79.7% |
| ADDRESS | 21 | 19 | 90.5% | 6 | 76.0% |
| DL | 1 | 1 | 100.0% | 1 | 50.0% |
| **All PII (incl. names/addresses)** | 209 | 156 | **74.6%** | 40 | |

**PII characters left visible (leak):** 20.3% overall; AADHAAR 12.0%, ADDRESS 14.7%, BANK_ACCT 36.6%, CARD 18.6%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 50.0%, NAME 21.1%, PAN 2.0%, PASSPORT 0.0%, PHONE 43.3%, UPI 26.9%, VEHICLE 0.0%, VOTER_ID 50.0%

**Rule-label recall by source:** chat 67.3%, doc 72.4%

**Latency per message:** mean 48.013 ms · p95 57.445 ms · p99 61.829 ms

## Sample misses

- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `sureshiyer@superyes` (handwritten)
- UPI: `9845012345@ybl` (handwritten)
- UPI: `kavya.r@okhdfcbank` (handwritten)
- AADHAAR: `9973 0911 4173` (handwritten)
- BANK_ACCT: `50100234567812` (handwritten)
- ADDRESS: `3rd house after ramu tea stall, blue gate, Vidyaranyapura` (handwritten)
- NAME: `Divya` (handwritten)
- NAME: `Imran` (handwritten)
- NAME: `Sanjay` (handwritten)
- PHONE: `7019234412` (handwritten)
- IP: `49.207.12.4` (handwritten)
- PHONE: `nine eight four five zero one two three four five` (handwritten)
- PHONE: `9845012399` (handwritten)
- NAME: `Abdul Rahman` (handwritten)
- NAME: `Vikram Singh Rathore` (handwritten)
- ADDRESS: `Hanuman temple, opp SBI ATM, Malleshwaram 18th cross` (handwritten)
- NAME: `Tanvi` (handwritten)
- PHONE: `9611234567` (handwritten)
- NAME: `Shalini` (handwritten)
- PHONE: `7353112233` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- CARD: `8137929841622946` (handwritten)
- PHONE: `94480 55123` (handwritten)
- VOTER_ID: `ABX5512309` (handwritten)
- PHONE: `9845098450` (handwritten)
- UPI: `priyanka.c@oksbi` (handwritten)
- PHONE: `nine eight one one zero four four three two one` (handwritten)
- NAME: `Ritu Arora` (handwritten)
- NAME: `Ramdas Pawar` (handwritten)
- PHONE: `9821001234` (handwritten)
- PHONE: `9900112233` (handwritten)
- NAME: `Arun Kumar` (handwritten)
- PHONE: `9845001122` (handwritten)
- NAME: `Zainab Qureshi` (handwritten)
- PHONE: `9886112233` (handwritten)
- NAME: `Teresa Fernandes` (handwritten)
- PHONE: `9123456780` (handwritten)

## Sample false alarms

- UPI: `UPI` (handwritten)
- EMAIL: `sureshiyer@superyes` (handwritten)
- EMAIL: `9845012345@ybl` (handwritten)
- PHONE: `9973 0911 4173` (handwritten)
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
- VEHICLE: `94480 55123` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Customer` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `u_88213` (handwritten)
- EMAIL: `priyanka.c@oksbi` (handwritten)
- NAME: `Agent` (handwritten)
- NAME: `Agent` (handwritten)
- PHONE: `number` (handwritten)
- PAN: `PAN card copy` (handwritten)
- AADHAAR: `XXXX XXXX 8158` (handwritten)
- ADDRESS: `Address` (handwritten)
- DL: `9821001234` (handwritten)
- PAN: `22` (handwritten)
- DOB: `1990` (handwritten)
- NAME: `______` (handwritten)
- ADDRESS: `address` (handwritten)
- VEHICLE: `KMC-44512` (handwritten)
- NAME: `Consumer` (handwritten)
- AADHAAR: `9845076543` (handwritten)
- EMAIL: `customercare@shopkart.in` (handwritten)
