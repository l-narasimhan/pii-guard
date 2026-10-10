# Piiranha: data/handwritten.jsonl

135 examples (97 chat, 38 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 8 | 3 | 37.5% | 12 | 20.0% |
| PAN | 5 | 0 | 0.0% | 1 | 0.0% |
| GSTIN | 5 | 0 | 0.0% | 0 | – |
| PHONE | 46 | 8 | 17.4% | 3 | 72.7% |
| EMAIL | 11 | 9 | 81.8% | 0 | 100.0% |
| UPI | 4 | 0 | 0.0% | 0 | – |
| CARD | 5 | 5 | 100.0% | 2 | 71.4% |
| BANK_ACCT | 8 | 6 | 75.0% | 7 | 46.2% |
| PASSPORT | 2 | 0 | 0.0% | 0 | – |
| VOTER_ID | 2 | 0 | 0.0% | 0 | – |
| VEHICLE | 5 | 0 | 0.0% | 0 | – |
| DOB | 7 | 7 | 100.0% | 0 | 100.0% |
| IP | 2 | 0 | 0.0% | 0 | – |
| **Rule labels total** | 110 | 38 | **34.5%** | 25 | **60.3%** |
| NAME | 77 | 61 | 79.2% | 4 | 93.8% |
| ADDRESS | 21 | 21 | 100.0% | 4 | 84.0% |
| DL | 1 | 1 | 100.0% | 6 | 14.3% |
| **All PII (incl. names/addresses)** | 209 | 121 | **57.9%** | 39 | |

**PII characters left visible (leak):** 36.0% overall; AADHAAR 14.0%, ADDRESS 29.6%, BANK_ACCT 21.5%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 21.1%, GSTIN 100.0%, IP 36.4%, NAME 21.3%, PAN 60.0%, PASSPORT 100.0%, PHONE 65.1%, UPI 85.1%, VEHICLE 100.0%, VOTER_ID 50.0%

**Rule-label recall by source:** chat 40.4%, doc 29.3%

**Latency per message:** mean 31.016 ms · p95 40.997 ms · p99 122.939 ms

## Sample misses

- NAME: `priya` (handwritten)
- PHONE: `9845012345` (handwritten)
- PHONE: `98450 77821` (handwritten)
- PHONE: `98450 1234O` (handwritten)
- PHONE: `99016` (handwritten)
- PHONE: `44328` (handwritten)
- UPI: `sureshiyer@superyes` (handwritten)
- UPI: `9845012345@ybl` (handwritten)
- UPI: `kavya.r@okhdfcbank` (handwritten)
- AADHAAR: `3588-1399-8697` (handwritten)
- AADHAAR: `9973 0911 4173` (handwritten)
- PAN: `AAKPV 4321 Q` (handwritten)
- PAN: `bqrps7788l` (handwritten)
- GSTIN: `10AAKPV4321Q8Z7` (handwritten)
- NAME: `Lakshmi` (handwritten)
- PHONE: `9741203345` (handwritten)
- PHONE: `7019234412` (handwritten)
- VEHICLE: `KA51AB4321` (handwritten)
- VEHICLE: `MH 12 DE 4567` (handwritten)
- PASSPORT: `M1234567` (handwritten)
- VOTER_ID: `TNX4421980` (handwritten)
- IP: `49.207.12.4` (handwritten)
- PHONE: `nine eight four five zero one two three four five` (handwritten)
- PHONE: `9663301122` (handwritten)
- PHONE: `9008123456` (handwritten)
- PHONE: `9845012399` (handwritten)
- PHONE: `8105 223 344` (handwritten)
- PHONE: `9611234567` (handwritten)
- NAME: `Anita` (handwritten)
- NAME: `Shalini` (handwritten)
- PHONE: `7353112233` (handwritten)
- PAN: `CXZPM1029K` (handwritten)
- AADHAAR: `6472 9405 5765` (handwritten)
- PHONE: `94480 55123` (handwritten)
- PHONE: `7019988776` (handwritten)
- PAN: `AAKPV4321Q` (handwritten)
- PHONE: `98450 12345` (handwritten)
- GSTIN: `24CXZPM1029K4ZW` (handwritten)
- PHONE: `9822012345` (handwritten)
- NAME: `Imran Khan` (handwritten)

## Sample false alarms

- AADHAAR: ` 98450 1234O` (handwritten)
- BANK_ACCT: ` 9845012345` (handwritten)
- BANK_ACCT: `9973 0911 4173` (handwritten)
- AADHAAR: ` AAKPV 4321 Q` (handwritten)
- ADDRESS: ` Jayanagar` (handwritten)
- BANK_ACCT: ` 783420019812` (handwritten)
- BANK_ACCT: ` 9536 4556 8159` (handwritten)
- CARD: `198765012345678` (handwritten)
- ADDRESS: ` Whitefield` (handwritten)
- NAME: ` Ganesh Chaturthi` (handwritten)
- AADHAAR: ` TNX4421980` (handwritten)
- AADHAAR: ` 49.` (handwritten)
- CARD: ` 403-1234567-7654321` (handwritten)
- AADHAAR: ` utr 412398765432` (handwritten)
- NAME: ` Hanuman Jayanti` (handwritten)
- DL: ` 8-2` (handwritten)
- AADHAAR: `-293/8` (handwritten)
- DL: `2` (handwritten)
- BANK_ACCT: ` 7353112233` (handwritten)
- AADHAAR: ` CXZPM1029K` (handwritten)
- PHONE: `6472 9405 5765` (handwritten)
- ADDRESS: ` Murugan` (handwritten)
- AADHAAR: ` 94480 55123` (handwritten)
- PAN: `=103.21.44.9` (handwritten)
- NAME: ` Mahalaxmi` (handwritten)
- DL: ` 9810077665` (handwritten)
- DL: ` 9821001234` (handwritten)
- PHONE: ` 8978-8093-2083` (handwritten)
- BANK_ACCT: ` 004512` (handwritten)
- DL: `9845001122` (handwritten)
- DL: `9886112233` (handwritten)
- NAME: ` Murugan Stores` (handwritten)
- ADDRESS: ` Koramangala` (handwritten)
- BANK_ACCT: ` 783420019900` (handwritten)
- AADHAAR: ` 1120034455` (handwritten)
- AADHAAR: `123450987612345678` (handwritten)
- AADHAAR: ` 9739912345` (handwritten)
- AADHAAR: ` 9880011223` (handwritten)
- PHONE: `
8488 7663 4407` (handwritten)
