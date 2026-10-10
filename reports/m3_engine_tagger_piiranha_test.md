# Rules + tagger(tagger-piiranha): data/test.jsonl

2000 examples (1191 chat, 809 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 198 | 198 | 100.0% | 0 | 100.0% |
| PAN | 91 | 91 | 100.0% | 2 | 97.8% |
| GSTIN | 36 | 36 | 100.0% | 0 | 100.0% |
| PHONE | 1680 | 1680 | 100.0% | 4 | 99.8% |
| EMAIL | 338 | 338 | 100.0% | 0 | 100.0% |
| UPI | 211 | 211 | 100.0% | 0 | 100.0% |
| CARD | 162 | 162 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 39 | 39 | 100.0% | 8 | 83.0% |
| PASSPORT | 45 | 45 | 100.0% | 0 | 100.0% |
| VOTER_ID | 165 | 165 | 100.0% | 0 | 100.0% |
| VEHICLE | 313 | 313 | 100.0% | 0 | 100.0% |
| DOB | 276 | 276 | 100.0% | 0 | 100.0% |
| IP | 40 | 40 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 3594 | 3594 | **100.0%** | 14 | **99.6%** |
| NAME | 2044 | 2040 | 99.8% | 125 | 94.2% |
| ADDRESS | 129 | 129 | 100.0% | 155 | 45.4% |
| DL | 40 | 40 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 5807 | 5803 | **99.9%** | 294 | |

**PII characters left visible (leak):** 0.0% overall; AADHAAR 0.0%, ADDRESS 0.1%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 0.0%, PAN 0.0%, PASSPORT 0.0%, PHONE 0.1%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 100.0%, doc 100.0%

**Latency per message:** mean 30.170 ms · p95 39.233 ms · p99 41.311 ms

## Sample misses

- NAME: `Chitra` (chat_66)
- NAME: `radha` (chat_66)
- NAME: `aditya` (chat_66)
- NAME: `Ayesha` (chat_66)

## Sample false alarms

- NAME: `haan` (chat_44)
- NAME: `uthata` (chat_39)
- ADDRESS: `682791` (rider_onboarding)
- ADDRESS: `141` (chat_9)
- ADDRESS: `pickup from` (chat_9)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `wahan bhejo` (chat_79)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_29)
- NAME: `haan` (chat_44)
- NAME: `uthata` (chat_39)
- ADDRESS: `Kamath Hotel, 122348` (rider_onboarding)
- ADDRESS: `201478` (rider_onboarding)
- NAME: `wahan bhejo` (chat_79)
- NAME: `wahan bhejo` (chat_79)
- ADDRESS: `380157` (rider_onboarding)
- ADDRESS: `226365` (rider_onboarding)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_29)
- ADDRESS: `Murugan Stores` (rider_onboarding)
- ADDRESS: `560679` (rider_onboarding)
- ADDRESS: `226994` (rider_onboarding)
- NAME: `haan` (chat_44)
- NAME: `wahan` (chat_79)
- BANK_ACCT: `sbin0423117` (chat_13)
- NAME: `haan` (chat_44)
- ADDRESS: `Meena Bazaar, 400530` (rider_onboarding)
- NAME: `haan` (chat_44)
- ADDRESS: `Meena Bazaar, 201583` (rider_onboarding)
- PAN: `sbin0815494` (chat_13)
- NAME: `haan` (chat_29)
- PHONE: `411210` (rider_onboarding)
- ADDRESS: `400303` (rider_onboarding)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_44)
- ADDRESS: `122361` (rider_onboarding)
- ADDRESS: `aashirvaad atta 5kg` (chat_9)
- NAME: `haan` (chat_44)
