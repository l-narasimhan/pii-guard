# GLiNER-PII: data/test.jsonl

1500 examples (911 chat, 589 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 241 | 241 | 100.0% | 0 | 100.0% |
| PAN | 96 | 94 | 97.9% | 0 | 100.0% |
| GSTIN | 76 | 76 | 100.0% | 0 | 100.0% |
| PHONE | 593 | 525 | 88.5% | 77 | 87.2% |
| EMAIL | 414 | 414 | 100.0% | 11 | 97.4% |
| UPI | 179 | 168 | 93.9% | 5 | 97.1% |
| CARD | 189 | 187 | 98.9% | 1 | 99.5% |
| BANK_ACCT | 79 | 79 | 100.0% | 31 | 71.8% |
| PASSPORT | 65 | 65 | 100.0% | 0 | 100.0% |
| VOTER_ID | 164 | 164 | 100.0% | 0 | 100.0% |
| VEHICLE | 356 | 326 | 91.6% | 5 | 98.5% |
| DOB | 286 | 286 | 100.0% | 0 | 100.0% |
| IP | 78 | 78 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 2816 | 2703 | **96.0%** | 130 | **95.4%** |
| NAME | 1121 | 914 | 81.5% | 314 | 74.4% |
| ADDRESS | 83 | 38 | 45.8% | 75 | 33.6% |
| DL | 0 | 0 | – | 3 | 0.0% |
| **All PII (incl. names/addresses)** | 4020 | 3655 | **90.9%** | 522 | |

**Rule-label recall by source:** chat 93.3%, doc 97.2%

**Latency per message:** mean 49.086 ms · p95 55.696 ms · p99 59.232 ms

## Sample misses

- NAME: `Prakash Desai` (chat_19)
- NAME: `Irfan Nair` (payment_receipt)
- NAME: `Pooja Fernandes` (payment_receipt)
- PHONE: `76891-21867` (chat_24)
- VEHICLE: `KL29N9558` (chat_19)
- NAME: `Naveen D. Mukherjee` (chat_44)
- NAME: `Manoj Thomas` (chat_19)
- NAME: `Durga Dutta` (chat_19)
- VEHICLE: `TS26V6350` (chat_19)
- NAME: `Balaji E. Sethi` (rider_onboarding)
- ADDRESS: `shanti kunj apartments, flat c-175, near bus stand, sector 137 201984` (chat_9)
- NAME: `Rekha Kamath` (payment_receipt)
- PHONE: `08444659003` (rider_onboarding)
- NAME: `Kunal P. Bhatia` (payment_receipt)
- ADDRESS: `H.No. 1-3-355/55, 100 Feet Road, Sector 18, Noida 201613` (chat_9)
- NAME: `Ganesh Pillai` (chat_19)
- PHONE: `06825927440` (rider_onboarding)
- PHONE: `6044401854` (rider_onboarding)
- ADDRESS: `#207, 9th cross, 1th main, thane west, thane 400323` (chat_9)
- NAME: `Ayesha Dubey` (payment_receipt)
- NAME: `S. Pillai` (payment_receipt)
- NAME: `S. Khan` (payment_receipt)
- ADDRESS: `mantri espana, flat d-753, near masjid, indira nagar 226882` (chat_9)
- NAME: `S. Grewal` (rider_onboarding)
- NAME: `Teresa Khan` (payment_receipt)
- NAME: `Senthil Ansari` (rider_onboarding)
- NAME: `Diya Kapoor` (payment_receipt)
- ADDRESS: `H.No. 3-9-135/49, Link Road, Andheri West, Mumbai 400730` (chat_9)
- NAME: `Meera Thakur` (payment_receipt)
- NAME: `farhan goyal` (chat_19)
- VEHICLE: `ka48xb7214` (chat_19)
- NAME: `Chitra Jadhav` (rider_onboarding)
- PHONE: `6352859167` (chat_24)
- NAME: `manoj r. rodrigues` (chat_19)
- VEHICLE: `rj-06-j-6273` (chat_19)
- NAME: `Dinesh Kamath` (chat_19)
- VEHICLE: `GJ10VE4984` (chat_19)
- NAME: `Pooja Fernandes` (chat_44)
- NAME: `Sanjay Deshpande` (chat_19)
- UPI: `meenakshi.s@ybl` (payment_receipt)

## Sample false alarms

- PHONE: `1800-419-0505` (chat_39)
- NAME: `agent` (chat_44)
- NAME: `customer` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `customer` (chat_44)
- ADDRESS: `Lakshmi General Stores, 560998` (rider_onboarding)
- ADDRESS: `Krishna Dairy` (chat_17)
- NAME: `agent` (chat_44)
- NAME: `customer` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `agent` (chat_44)
- NAME: `customer` (chat_44)
- NAME: `Customer` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `Customer` (chat_44)
- BANK_ACCT: `IFSC UTIB0235060` (chat_13)
- ADDRESS: `Fatima Bakery, 110194` (rider_onboarding)
- NAME: `haan ji` (chat_29)
- NAME: `agent` (chat_44)
- NAME: `customer` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `customer` (chat_44)
- PHONE: `1800-419-0505` (chat_39)
- NAME: `haan ji` (chat_29)
- PHONE: `1800 102 7777` (chat_39)
- BANK_ACCT: `IFSC UTIB0425048` (chat_13)
- ADDRESS: `joseph & co.` (chat_17)
- PHONE: `1800 208 9898` (chat_39)
- ADDRESS: `Patel Brothers Hardware, 380166` (rider_onboarding)
- BANK_ACCT: `IFSC KKBK0375263` (chat_13)
- VEHICLE: `#207` (chat_9)
- PHONE: `1800-123-4455` (chat_39)
- NAME: `haan ji` (chat_29)
- BANK_ACCT: `IFSC PUNB0720386` (chat_13)
- ADDRESS: `Ganesh Traders, 700774` (rider_onboarding)
- BANK_ACCT: `IFSC SBIN0795929` (chat_13)
- NAME: `haan ji` (chat_29)
- NAME: `haan ji` (chat_29)
- NAME: `haan ji` (chat_29)
- ADDRESS: `Murugan Stores, 400048` (rider_onboarding)
