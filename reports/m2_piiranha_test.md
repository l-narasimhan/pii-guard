# Piiranha: data/test.jsonl

1500 examples (911 chat, 589 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 241 | 42 | 17.4% | 304 | 12.1% |
| PAN | 96 | 0 | 0.0% | 24 | 0.0% |
| GSTIN | 76 | 0 | 0.0% | 0 | – |
| PHONE | 593 | 212 | 35.8% | 126 | 62.7% |
| EMAIL | 414 | 414 | 100.0% | 0 | 100.0% |
| UPI | 179 | 0 | 0.0% | 0 | – |
| CARD | 189 | 163 | 86.2% | 57 | 74.1% |
| BANK_ACCT | 79 | 73 | 92.4% | 33 | 68.9% |
| PASSPORT | 65 | 0 | 0.0% | 0 | – |
| VOTER_ID | 164 | 0 | 0.0% | 0 | – |
| VEHICLE | 356 | 0 | 0.0% | 0 | – |
| DOB | 286 | 286 | 100.0% | 0 | 100.0% |
| IP | 78 | 0 | 0.0% | 0 | – |
| **Rule labels total** | 2816 | 1190 | **42.3%** | 544 | **68.6%** |
| NAME | 1121 | 875 | 78.1% | 19 | 97.9% |
| ADDRESS | 83 | 83 | 100.0% | 300 | 21.7% |
| DL | 0 | 0 | – | 55 | 0.0% |
| **All PII (incl. names/addresses)** | 4020 | 2148 | **53.4%** | 918 | |

**Rule-label recall by source:** chat 41.1%, doc 42.8%

**Latency per message:** mean 31.920 ms · p95 41.440 ms · p99 43.325 ms

## Sample misses

- IP: `49.198.159.93` (chat_20)
- VEHICLE: `MH 39 WP 6594` (chat_19)
- PAN: `TLIPN5276U` (chat_36)
- NAME: `ishita khanna` (chat_13)
- UPI: `pooja.f75@okicici` (payment_receipt)
- NAME: `simran tiwari` (chat_24)
- PHONE: `76891-21867` (chat_24)
- VEHICLE: `KL29N9558` (chat_19)
- GSTIN: `33BBRPP8532C1ZI` (chat_17)
- PHONE: `8126 741 377` (chat_44)
- NAME: `shanti pereira` (chat_44)
- VEHICLE: `TN38PM5521` (rider_onboarding)
- GSTIN: `19CKJPS6870O5ZV` (chat_17)
- PHONE: `6253166588` (rider_onboarding)
- VEHICLE: `AP 18 VE 9843` (rider_onboarding)
- AADHAAR: `4120 5691 9597` (rider_onboarding)
- NAME: `Ramesh Mehta` (rider_onboarding)
- PHONE: `8357192167` (rider_onboarding)
- PHONE: `96292 53422` (chat_24)
- PHONE: `06533923513` (chat_44)
- NAME: `mary sethi` (chat_44)
- VEHICLE: `AP-58-UT-1521` (rider_onboarding)
- VOTER_ID: `MNE3560386` (rider_onboarding)
- VEHICLE: `MH 08 X 0626` (rider_onboarding)
- VOTER_ID: `BNY2714169` (rider_onboarding)
- AADHAAR: `6930 8508 7804` (rider_onboarding)
- PAN: `pmbpt0866s` (chat_36)
- PHONE: `09871640579` (rider_onboarding)
- AADHAAR: `3485 7386 4813` (rider_onboarding)
- VEHICLE: `DL40JU7054` (rider_onboarding)
- NAME: `Prakash Malhotra` (rider_onboarding)
- UPI: `priya.j@oksbi` (payment_receipt)
- PAN: `guhpd3829i` (chat_36)
- VEHICLE: `DL 11 BH 9961` (chat_19)
- VEHICLE: `TS26V6350` (chat_19)
- CARD: `5582 7590 8718 8799` (payment_receipt)
- UPI: `8756861923@axl` (payment_receipt)
- UPI: `9041047761@paytm` (payment_receipt)
- AADHAAR: `8869-7128-5650` (rider_onboarding)
- VEHICLE: `GJ 51 UT 3824` (rider_onboarding)

## Sample false alarms

- PAN: ` 49.198.159.93` (chat_20)
- PHONE: ` 1800-419-0505` (chat_39)
- BANK_ACCT: ` 006-1898095-1596898` (payment_receipt)
- ADDRESS: ` 76891-21867` (chat_24)
- ADDRESS: ` Murugan` (chat_17)
- DL: ` 33BBRPP8532C1ZI` (chat_17)
- ADDRESS: ` Lakshmi` (rider_onboarding)
- ADDRESS: ` 560998` (rider_onboarding)
- DL: ` 19CKJPS6870O5ZV` (chat_17)
- PHONE: ` 4120 5691 9597` (rider_onboarding)
- ADDRESS: ` Fatima Bakery, 380676` (rider_onboarding)
- PAN: ` 96292 53422` (chat_24)
- AADHAAR: ` 06533923513` (chat_44)
- AADHAAR: ` MNE3560386` (rider_onboarding)
- ADDRESS: ` Lakshmi` (rider_onboarding)
- ADDRESS: ` 122259` (rider_onboarding)
- AADHAAR: ` BNY2714169` (rider_onboarding)
- PHONE: ` 6930 8508 7804` (rider_onboarding)
- PHONE: ` 3485 7386 4813` (rider_onboarding)
- ADDRESS: ` 380017` (rider_onboarding)
- BANK_ACCT: `209733749` (chat_4)
- AADHAAR: ` 5582 7590 8718 8` (payment_receipt)
- CARD: ` 434-8476848-4650399` (payment_receipt)
- PHONE: ` 8869-7128-5650` (rider_onboarding)
- ADDRESS: ` Fatima Bakery, 110194` (rider_onboarding)
- PHONE: ` 4913-9569-2469` (rider_onboarding)
- AADHAAR: ` MSX0448973` (rider_onboarding)
- AADHAAR: ` 117.219.90.207` (chat_20)
- PHONE: ` 1800-419-0505` (chat_39)
- CARD: ` 500821092784` (rider_onboarding)
- AADHAAR: ` 122.225.13.53` (chat_20)
- DL: ` 7993 072 257` (chat_24)
- CARD: ` 409-1988143-8708755` (payment_receipt)
- AADHAAR: ` 15` (chat_17)
- AADHAAR: `pk7216d5` (chat_17)
- AADHAAR: `6` (chat_17)
- AADHAAR: ` 157.99.157.205` (chat_20)
- AADHAAR: ` AAN4125688` (rider_onboarding)
- ADDRESS: ` Ramesh` (rider_onboarding)
- ADDRESS: ` 110459` (rider_onboarding)
