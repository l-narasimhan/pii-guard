# gemma-4-e4b-it-4bit: data/test_sample300.jsonl

300 examples (181 chat, 119 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 36 | 36 | 100.0% | 0 | 100.0% |
| PAN | 10 | 2 | 20.0% | 0 | 100.0% |
| GSTIN | 6 | 0 | 0.0% | 0 | – |
| PHONE | 269 | 144 | 53.5% | 0 | 100.0% |
| EMAIL | 49 | 45 | 91.8% | 1 | 97.8% |
| UPI | 18 | 17 | 94.4% | 0 | 100.0% |
| CARD | 19 | 0 | 0.0% | 0 | – |
| BANK_ACCT | 3 | 0 | 0.0% | 0 | – |
| PASSPORT | 8 | 0 | 0.0% | 0 | – |
| VOTER_ID | 27 | 24 | 88.9% | 0 | 100.0% |
| VEHICLE | 48 | 39 | 81.2% | 0 | 100.0% |
| DOB | 45 | 36 | 80.0% | 0 | 100.0% |
| IP | 7 | 7 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 545 | 350 | **64.2%** | 1 | **99.7%** |
| NAME | 303 | 281 | 92.7% | 0 | 100.0% |
| ADDRESS | 20 | 3 | 15.0% | 0 | 100.0% |
| DL | 5 | 5 | 100.0% | 1 | 83.3% |
| **All PII (incl. names/addresses)** | 873 | 639 | **73.2%** | 2 | |

**PII characters left visible (leak):** 27.8% overall; AADHAAR 0.0%, ADDRESS 84.8%, BANK_ACCT 100.0%, CARD 100.0%, DL 0.0%, DOB 20.0%, EMAIL 10.1%, GSTIN 100.0%, IP 0.0%, NAME 5.5%, PAN 80.0%, PASSPORT 100.0%, PHONE 42.6%, UPI 0.0%, VEHICLE 16.5%, VOTER_ID 11.1%

**Rule-label recall by source:** chat 55.1%, doc 67.0%

**Latency per message:** mean 1311.262 ms · p95 3641.807 ms · p99 4638.331 ms

## Sample misses

- PHONE: `8986424515` (rider_onboarding)
- PHONE: `8549996690` (visitor_log)
- PHONE: `+91 69471 59685` (visitor_log)
- PHONE: `75459 63131` (visitor_log)
- ADDRESS: `behind Ganesh kirana, 6th street, Hinjewadi 411003` (chat_66)
- NAME: `Jyoti` (chat_66)
- PHONE: `022 2660 7954` (chat_74)
- DOB: `26 July 1970` (rider_onboarding)
- PAN: `QLVPA3051E` (chat_36)
- PHONE: `7547528816` (rider_onboarding)
- NAME: `Priya` (chat_50)
- PHONE: `62728` (chat_71)
- PHONE: `62728` (chat_71)
- PHONE: `86548` (chat_71)
- ADDRESS: `opp Raju tea stall, green building last floor, Aliganj` (chat_66)
- NAME: `Imran` (chat_66)
- PHONE: `80327 75803` (rider_onboarding)
- VEHICLE: `gj 48 m 6494` (chat_19)
- PHONE: `+91 92663 16055` (rider_onboarding)
- CARD: `6081-1830-8738-1334` (payment_receipt)
- PHONE: `+91 85677 20819` (rider_onboarding)
- PHONE: `7058155193` (rider_onboarding)
- PHONE: `+91 81657 64228` (visitor_log)
- PHONE: `84098 42749` (visitor_log)
- PHONE: `88065-80056` (visitor_log)
- PHONE: `+918252470484` (visitor_log)
- PHONE: `6032 991 643` (visitor_log)
- PHONE: `68452-90264` (visitor_log)
- PHONE: `9615370184` (visitor_log)
- CARD: `8102864241261063` (payment_receipt)
- CARD: `8156770001327611` (payment_receipt)
- PASSPORT: `R8404696` (chat_18)
- ADDRESS: `opp Sagar hotel, green building 1st floor, Navrangpura` (chat_66)
- NAME: `Sunita` (chat_66)
- PHONE: `75636-11955` (rider_onboarding)
- VOTER_ID: `DSM3513584` (rider_onboarding)
- PAN: `ewzpg7192u` (chat_36)
- CARD: `5439 6198 3063 0205` (payment_receipt)
- PHONE: `8796 629 953` (visitor_log)
- PHONE: `9932 732 863` (visitor_log)

## Sample false alarms

- EMAIL: `rohit26@mbk` (chat_83)
- DL: `DL 60 MN 1456` (rider_onboarding)

Gemma stats: {"calls": 433, "returned": 780, "not_in_text": 5, "bad_json": 0, "bad_label": 0}
