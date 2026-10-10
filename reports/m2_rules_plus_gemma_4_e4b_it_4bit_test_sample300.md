# Rules + gemma-4-e4b-it-4bit: data/test_sample300.jsonl

300 examples (181 chat, 119 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 36 | 36 | 100.0% | 0 | 100.0% |
| PAN | 10 | 10 | 100.0% | 0 | 100.0% |
| GSTIN | 6 | 6 | 100.0% | 0 | 100.0% |
| PHONE | 269 | 259 | 96.3% | 0 | 100.0% |
| EMAIL | 49 | 45 | 91.8% | 1 | 97.8% |
| UPI | 18 | 17 | 94.4% | 0 | 100.0% |
| CARD | 19 | 19 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 3 | 3 | 100.0% | 0 | 100.0% |
| PASSPORT | 8 | 8 | 100.0% | 0 | 100.0% |
| VOTER_ID | 27 | 27 | 100.0% | 0 | 100.0% |
| VEHICLE | 48 | 48 | 100.0% | 0 | 100.0% |
| DOB | 45 | 45 | 100.0% | 0 | 100.0% |
| IP | 7 | 7 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 545 | 530 | **97.2%** | 1 | **99.8%** |
| NAME | 303 | 281 | 92.7% | 0 | 100.0% |
| ADDRESS | 20 | 3 | 15.0% | 0 | 100.0% |
| DL | 5 | 5 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 873 | 819 | **93.8%** | 1 | |

**PII characters left visible (leak):** 10.0% overall; AADHAAR 0.0%, ADDRESS 84.8%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 10.1%, GSTIN 0.0%, IP 0.0%, NAME 5.5%, PAN 0.0%, PASSPORT 0.0%, PHONE 2.3%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 88.2%, doc 100.0%

**Latency per message:** mean 0.049 ms · p95 0.109 ms · p99 0.133 ms

## Sample misses

- ADDRESS: `behind Ganesh kirana, 6th street, Hinjewadi 411003` (chat_66)
- NAME: `Jyoti` (chat_66)
- PHONE: `022 2660 7954` (chat_74)
- NAME: `Priya` (chat_50)
- PHONE: `62728` (chat_71)
- ADDRESS: `opp Raju tea stall, green building last floor, Aliganj` (chat_66)
- NAME: `Imran` (chat_66)
- ADDRESS: `opp Sagar hotel, green building 1st floor, Navrangpura` (chat_66)
- NAME: `Sunita` (chat_66)
- NAME: `Kusum Fernandes` (chat_17)
- ADDRESS: `opp indian oil pump, white building 1st floor, aliganj` (chat_90)
- EMAIL: `hemas at gmail dot com` (chat_79)
- PHONE: `044-4304 5020` (chat_74)
- NAME: `Lokesh Dhillon` (chat_17)
- NAME: `Jasvinder Verma` (payment_receipt)
- NAME: `Sneha` (chat_50)
- PHONE: `68238` (chat_71)
- ADDRESS: `B-1413, Sri Lakshmi Nilayam, Indira Nagar` (chat_9)
- NAME: `Kiran Iyer` (rider_onboarding)
- UPI: `rohit26@mbk` (chat_83)
- NAME: `Srinivas E. Fernandes` (chat_17)
- ADDRESS: `gali no 1, church ke peeche, malviya nagar` (chat_90)
- EMAIL: `bhavana.khanna[at]outlook.com` (chat_79)
- NAME: `Thomas` (chat_50)
- PHONE: `044-5879 2712` (chat_74)
- ADDRESS: `11ne cross, Durga mandir hatra, Malviya Nagar` (chat_66)
- NAME: `Ritesh` (chat_66)
- PHONE: `76921` (chat_71)
- ADDRESS: `flat d-984, raheja vihar, near water tank, navrangpura, ahmedabad - 380370` (chat_9)
- NAME: `arjun` (chat_50)
- PHONE: `62878` (chat_71)
- ADDRESS: `Flat D-1467, Hiranandani Gardens, near bus stand, Mansarovar, Jaipur - 302231` (chat_9)
- NAME: `Shalini Gowda` (chat_17)
- PHONE: `81519` (chat_71)
- ADDRESS: `b-145, brigade metropolis, thane west` (chat_9)
- ADDRESS: `house with yellow gate near iyengar bakery, kaloor` (chat_90)
- EMAIL: `arindam.rodrigues (at) gmail.com` (chat_79)
- PHONE: `87017` (chat_71)
- NAME: `Revathi Roy` (chat_17)
- ADDRESS: `plot 382, gandhi marg, near water tank, sector 137, noida` (chat_9)

## Sample false alarms

- EMAIL: `rohit26@mbk` (chat_83)

Gemma stats: {"calls": 433, "returned": 780, "not_in_text": 5, "bad_json": 0, "bad_label": 0}
