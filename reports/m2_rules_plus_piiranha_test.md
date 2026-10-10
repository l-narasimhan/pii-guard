# Rules + Piiranha: data/test.jsonl

1500 examples (911 chat, 589 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 241 | 241 | 100.0% | 13 | 94.9% |
| PAN | 96 | 96 | 100.0% | 0 | 100.0% |
| GSTIN | 76 | 76 | 100.0% | 0 | 100.0% |
| PHONE | 593 | 586 | 98.8% | 41 | 93.5% |
| EMAIL | 414 | 414 | 100.0% | 0 | 100.0% |
| UPI | 179 | 179 | 100.0% | 0 | 100.0% |
| CARD | 189 | 189 | 100.0% | 43 | 81.5% |
| BANK_ACCT | 79 | 79 | 100.0% | 21 | 79.0% |
| PASSPORT | 65 | 65 | 100.0% | 0 | 100.0% |
| VOTER_ID | 164 | 164 | 100.0% | 0 | 100.0% |
| VEHICLE | 356 | 356 | 100.0% | 0 | 100.0% |
| DOB | 286 | 286 | 100.0% | 0 | 100.0% |
| IP | 78 | 78 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 2816 | 2809 | **99.8%** | 118 | **96.0%** |
| NAME | 1121 | 875 | 78.1% | 19 | 97.9% |
| ADDRESS | 83 | 83 | 100.0% | 271 | 23.4% |
| **All PII (incl. names/addresses)** | 4020 | 3767 | **93.7%** | 408 | |

**Rule-label recall by source:** chat 99.2%, doc 100.0%

**Latency per message:** mean 32.731 ms · p95 42.541 ms · p99 44.919 ms

## Sample misses

- NAME: `ishita khanna` (chat_13)
- NAME: `simran tiwari` (chat_24)
- NAME: `shanti pereira` (chat_44)
- NAME: `Ramesh Mehta` (rider_onboarding)
- NAME: `mary sethi` (chat_44)
- NAME: `Prakash Malhotra` (rider_onboarding)
- NAME: `n. banerjee` (chat_44)
- NAME: `Nandini Roy` (rider_onboarding)
- NAME: `meenakshi kamath` (chat_17)
- NAME: `Fatima Bose` (rider_onboarding)
- NAME: `Rekha Naidu` (rider_onboarding)
- NAME: `rahul t. sethi` (chat_24)
- NAME: `siddharth s. ghosh` (chat_13)
- NAME: `Pooja Sharma` (rider_onboarding)
- NAME: `George D. Dutta` (rider_onboarding)
- NAME: `Bharati Verma` (rider_onboarding)
- NAME: `Hema V. Shah` (rider_onboarding)
- NAME: `anita joshi` (chat_44)
- NAME: `teresa fernandes` (chat_13)
- NAME: `S. Grewal` (rider_onboarding)
- NAME: `riya mahajan` (chat_44)
- NAME: `ramesh thakur` (chat_17)
- NAME: `farhan goyal` (chat_19)
- NAME: `Tanmoy Murthy` (rider_onboarding)
- NAME: `revathi kamath` (chat_17)
- NAME: `deepak gill` (chat_13)
- NAME: `abdul v. das` (chat_13)
- NAME: `manoj r. rodrigues` (chat_19)
- NAME: `N. Patel` (rider_onboarding)
- NAME: `Gurpreet Thomas` (rider_onboarding)
- NAME: `Mohan Bose` (rider_onboarding)
- NAME: `pradeep deshpande` (chat_17)
- NAME: `anil kaur` (chat_19)
- NAME: `N. Ghosh` (rider_onboarding)
- NAME: `vijay sandhu` (chat_13)
- NAME: `Varun Shetty` (payment_receipt)
- NAME: `Manpreet B. Murthy` (rider_onboarding)
- NAME: `vijay bisht` (chat_24)
- NAME: `priya c. bisht` (chat_44)
- NAME: `kavya patel` (chat_17)

## Sample false alarms

- PHONE: ` 1800-419-0505` (chat_39)
- BANK_ACCT: ` 006-1898095-1596898` (payment_receipt)
- ADDRESS: ` Murugan` (chat_17)
- ADDRESS: ` Lakshmi` (rider_onboarding)
- ADDRESS: ` 560998` (rider_onboarding)
- ADDRESS: ` Fatima Bakery, 380676` (rider_onboarding)
- ADDRESS: ` Lakshmi` (rider_onboarding)
- ADDRESS: ` 122259` (rider_onboarding)
- ADDRESS: ` 380017` (rider_onboarding)
- BANK_ACCT: `209733749` (chat_4)
- CARD: ` 434-8476848-4650399` (payment_receipt)
- ADDRESS: ` Fatima Bakery, 110194` (rider_onboarding)
- PHONE: ` 1800-419-0505` (chat_39)
- CARD: ` 409-1988143-8708755` (payment_receipt)
- ADDRESS: ` Ramesh` (rider_onboarding)
- ADDRESS: ` 110459` (rider_onboarding)
- NAME: ` Aashirvaad Atta 5kg` (chat_9)
- ADDRESS: ` Patel Brothers` (rider_onboarding)
- ADDRESS: ` 380166` (rider_onboarding)
- ADDRESS: ` Murugan` (rider_onboarding)
- ADDRESS: ` 682942` (rider_onboarding)
- PHONE: ` 1800-123-4455` (chat_39)
- ADDRESS: ` George D. Dutta` (rider_onboarding)
- ADDRESS: ` Ganesh Traders` (rider_onboarding)
- ADDRESS: ` 600867` (rider_onboarding)
- ADDRESS: ` Murugan` (rider_onboarding)
- ADDRESS: ` 400048` (rider_onboarding)
- ADDRESS: ` Patel Brothers` (rider_onboarding)
- ADDRESS: ` 500882` (rider_onboarding)
- NAME: ` Parle-G` (chat_9)
- AADHAAR: ` 30` (payment_receipt)
- ADDRESS: ` 302191` (rider_onboarding)
- PHONE: ` 1800-419-0505` (chat_39)
- ADDRESS: ` 122477` (rider_onboarding)
- ADDRESS: ` 122914` (rider_onboarding)
- ADDRESS: ` 500384` (rider_onboarding)
- ADDRESS: ` Lakshmi` (rider_onboarding)
- ADDRESS: ` 226893` (rider_onboarding)
- ADDRESS: ` Sai Ram Kirana, 201577` (rider_onboarding)
- NAME: ` Amul` (chat_9)
