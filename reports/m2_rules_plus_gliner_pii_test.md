# Rules + GLiNER-PII: data/test.jsonl

1500 examples (911 chat, 589 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 241 | 241 | 100.0% | 0 | 100.0% |
| PAN | 96 | 96 | 100.0% | 0 | 100.0% |
| GSTIN | 76 | 76 | 100.0% | 0 | 100.0% |
| PHONE | 593 | 586 | 98.8% | 77 | 88.4% |
| EMAIL | 414 | 414 | 100.0% | 0 | 100.0% |
| UPI | 179 | 179 | 100.0% | 5 | 97.3% |
| CARD | 189 | 189 | 100.0% | 1 | 99.5% |
| BANK_ACCT | 79 | 79 | 100.0% | 31 | 71.8% |
| PASSPORT | 65 | 65 | 100.0% | 0 | 100.0% |
| VOTER_ID | 164 | 164 | 100.0% | 0 | 100.0% |
| VEHICLE | 356 | 356 | 100.0% | 5 | 98.6% |
| DOB | 286 | 286 | 100.0% | 0 | 100.0% |
| IP | 78 | 78 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 2816 | 2809 | **99.8%** | 119 | **95.9%** |
| NAME | 1121 | 914 | 81.5% | 314 | 74.4% |
| ADDRESS | 83 | 38 | 45.8% | 75 | 33.6% |
| **All PII (incl. names/addresses)** | 4020 | 3761 | **93.6%** | 508 | |

**Rule-label recall by source:** chat 99.2%, doc 100.0%

**Latency per message:** mean 49.445 ms · p95 57.154 ms · p99 59.251 ms

## Sample misses

- NAME: `Prakash Desai` (chat_19)
- NAME: `Irfan Nair` (payment_receipt)
- NAME: `Pooja Fernandes` (payment_receipt)
- NAME: `Naveen D. Mukherjee` (chat_44)
- NAME: `Manoj Thomas` (chat_19)
- NAME: `Durga Dutta` (chat_19)
- NAME: `Balaji E. Sethi` (rider_onboarding)
- ADDRESS: `shanti kunj apartments, flat c-175, near bus stand, sector 137 201984` (chat_9)
- NAME: `Rekha Kamath` (payment_receipt)
- NAME: `Kunal P. Bhatia` (payment_receipt)
- ADDRESS: `H.No. 1-3-355/55, 100 Feet Road, Sector 18, Noida 201613` (chat_9)
- NAME: `Ganesh Pillai` (chat_19)
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
- NAME: `Chitra Jadhav` (rider_onboarding)
- NAME: `manoj r. rodrigues` (chat_19)
- NAME: `Dinesh Kamath` (chat_19)
- NAME: `Pooja Fernandes` (chat_44)
- NAME: `Sanjay Deshpande` (chat_19)
- NAME: `Kavitha Roy` (payment_receipt)
- NAME: `Bikash S. Yadav` (payment_receipt)
- ADDRESS: `Plot 128, 100 Feet Road, near masjid, Garia, Kolkata` (chat_9)
- NAME: `N. Patel` (rider_onboarding)
- NAME: `Kunal Srivastava` (chat_19)
- NAME: `anil kaur` (chat_19)
- NAME: `Salman M. Chettiar` (payment_receipt)
- NAME: `N. Ghosh` (rider_onboarding)
- NAME: `Jitendra Das` (chat_19)
- NAME: `Ayesha Shastri` (payment_receipt)
- ADDRESS: `flat b-917, raheja vihar, behind reliance fresh, malviya nagar, jaipur - 302007` (chat_9)

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
