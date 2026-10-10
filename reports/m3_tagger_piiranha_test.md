# tagger(tagger-piiranha): data/test.jsonl

2000 examples (1191 chat, 809 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 198 | 190 | 96.0% | 1 | 99.5% |
| PAN | 91 | 91 | 100.0% | 6 | 93.8% |
| GSTIN | 36 | 36 | 100.0% | 0 | 100.0% |
| PHONE | 1680 | 1680 | 100.0% | 28 | 98.4% |
| EMAIL | 338 | 338 | 100.0% | 0 | 100.0% |
| UPI | 211 | 211 | 100.0% | 1 | 99.5% |
| CARD | 162 | 162 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 39 | 39 | 100.0% | 16 | 70.9% |
| PASSPORT | 45 | 0 | 0.0% | 0 | – |
| VOTER_ID | 165 | 162 | 98.2% | 3 | 98.2% |
| VEHICLE | 313 | 313 | 100.0% | 14 | 95.7% |
| DOB | 276 | 276 | 100.0% | 0 | 100.0% |
| IP | 40 | 34 | 85.0% | 0 | 100.0% |
| **Rule labels total** | 3594 | 3532 | **98.3%** | 69 | **98.1%** |
| NAME | 2044 | 2041 | 99.9% | 126 | 94.2% |
| ADDRESS | 129 | 129 | 100.0% | 159 | 44.8% |
| DL | 40 | 40 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 5807 | 5742 | **98.9%** | 354 | |

**PII characters left visible (leak):** 0.5% overall; AADHAAR 0.0%, ADDRESS 0.1%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 16.3%, NAME 0.0%, PAN 0.0%, PASSPORT 71.7%, PHONE 0.0%, UPI 0.9%, VEHICLE 0.0%, VOTER_ID 1.3%

**Rule-label recall by source:** chat 93.1%, doc 99.9%

**Latency per message:** mean 30.966 ms · p95 40.670 ms · p99 43.780 ms

## Sample misses

- PASSPORT: `J2323765` (chat_18)
- PASSPORT: `G5374466` (chat_18)
- PASSPORT: `l6451258` (chat_18)
- AADHAAR: `776264566938` (chat_29)
- NAME: `Chitra` (chat_66)
- PASSPORT: `n4989013` (chat_18)
- PASSPORT: `h4926383` (chat_18)
- PASSPORT: `W3817613` (chat_18)
- PASSPORT: `T7894901` (chat_18)
- AADHAAR: `473245502408` (chat_29)
- PASSPORT: `r9648329` (chat_18)
- PASSPORT: `N1934911` (chat_18)
- PASSPORT: `e3725997` (chat_18)
- NAME: `radha` (chat_66)
- PASSPORT: `T7273603` (chat_18)
- PASSPORT: `p9240767` (chat_18)
- IP: `122.158.216.231` (chat_20)
- IP: `203.44.55.100` (chat_20)
- AADHAAR: `5815-2636-6967` (chat_29)
- AADHAAR: `732896236021` (chat_29)
- PASSPORT: `N9125937` (chat_18)
- PASSPORT: `w5267820` (chat_18)
- PASSPORT: `B4307424` (chat_18)
- PASSPORT: `H7113123` (chat_18)
- PASSPORT: `N7194381` (chat_18)
- PASSPORT: `R8404696` (chat_18)
- PASSPORT: `J4695033` (chat_18)
- PASSPORT: `P7158149` (chat_18)
- PASSPORT: `p8002444` (chat_18)
- PASSPORT: `C2828776` (chat_18)
- PASSPORT: `b6555190` (chat_18)
- PASSPORT: `P8804990` (chat_18)
- AADHAAR: `5247 8773 3549` (chat_29)
- PASSPORT: `F5757855` (chat_18)
- PASSPORT: `L6115458` (chat_18)
- PASSPORT: `A9221903` (chat_18)
- PASSPORT: `U9011438` (chat_18)
- PASSPORT: `H4706092` (chat_18)
- IP: `157.0.134.112` (chat_20)
- AADHAAR: `7489-7183-8896` (chat_29)

## Sample false alarms

- NAME: `haan` (chat_44)
- NAME: `uthata` (chat_39)
- ADDRESS: `2791` (rider_onboarding)
- ADDRESS: `141` (chat_9)
- ADDRESS: `pickup from` (chat_9)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_44)
- NAME: `wahan bhejo` (chat_79)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_44)
- VEHICLE: `6451258` (chat_18)
- NAME: `haan` (chat_29)
- BANK_ACCT: `776264566938` (chat_29)
- NAME: `haan` (chat_44)
- NAME: `uthata` (chat_39)
- ADDRESS: `Kamath Hotel, 122348` (rider_onboarding)
- ADDRESS: `78` (rider_onboarding)
- NAME: `wahan bhejo` (chat_79)
- NAME: `wahan bhejo` (chat_79)
- ADDRESS: `157` (rider_onboarding)
- VEHICLE: `W3817613` (chat_18)
- ADDRESS: `226365` (rider_onboarding)
- NAME: `haan` (chat_44)
- NAME: `haan` (chat_29)
- PHONE: `7152-3619-65` (chat_29)
- ADDRESS: `ugan Store` (rider_onboarding)
- ADDRESS: `560679` (rider_onboarding)
- ADDRESS: `226994` (rider_onboarding)
- NAME: `haan` (chat_44)
- NAME: `wahan` (chat_79)
- PAN: `bin0423` (chat_13)
- BANK_ACCT: `117` (chat_13)
- NAME: `haan` (chat_44)
- ADDRESS: `Meena Bazaar, 400530` (rider_onboarding)
- NAME: `haan` (chat_44)
- ADDRESS: `Meena Bazaar, 201583` (rider_onboarding)
- PAN: `bin0815494` (chat_13)
- NAME: `haan` (chat_29)
- BANK_ACCT: `473245502408` (chat_29)
- VEHICLE: `r9648329` (chat_18)
