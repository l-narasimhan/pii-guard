# Rules + gemma-4-e2b-it-4bit: data/test_sample300.jsonl

300 examples (188 chat, 112 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 42 | 42 | 100.0% | 0 | 100.0% |
| PAN | 19 | 19 | 100.0% | 0 | 100.0% |
| GSTIN | 20 | 20 | 100.0% | 0 | 100.0% |
| PHONE | 113 | 112 | 99.1% | 12 | 90.3% |
| EMAIL | 85 | 85 | 100.0% | 0 | 100.0% |
| UPI | 30 | 30 | 100.0% | 0 | 100.0% |
| CARD | 25 | 25 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 18 | 18 | 100.0% | 0 | 100.0% |
| PASSPORT | 20 | 20 | 100.0% | 0 | 100.0% |
| VOTER_ID | 30 | 30 | 100.0% | 0 | 100.0% |
| VEHICLE | 70 | 70 | 100.0% | 0 | 100.0% |
| DOB | 57 | 57 | 100.0% | 0 | 100.0% |
| IP | 19 | 19 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 548 | 547 | **99.8%** | 12 | **97.9%** |
| NAME | 219 | 187 | 85.4% | 0 | 100.0% |
| ADDRESS | 13 | 13 | 100.0% | 2 | 86.7% |
| **All PII (incl. names/addresses)** | 780 | 747 | **95.8%** | 14 | |

**PII characters left visible (leak):** 4.1% overall; AADHAAR 0.0%, ADDRESS 4.1%, BANK_ACCT 0.0%, CARD 0.0%, DOB 0.0%, EMAIL 0.0%, GSTIN 0.0%, IP 0.0%, NAME 14.5%, PAN 0.0%, PASSPORT 0.0%, PHONE 3.1%, UPI 0.0%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 99.5%, doc 100.0%

**Latency per message:** mean 0.054 ms · p95 0.100 ms · p99 0.124 ms

## Sample misses

- NAME: `Shalini Gill` (rider_onboarding)
- NAME: `Irfan Mukherjee` (chat_17)
- NAME: `Zainab P. Gowda` (rider_onboarding)
- NAME: `Ramesh Mehta` (rider_onboarding)
- NAME: `Pooja Murthy` (chat_17)
- NAME: `Nandini Naidu` (rider_onboarding)
- NAME: `Geeta Jadhav` (rider_onboarding)
- NAME: `h. desai` (chat_17)
- NAME: `Manoj Agarwal` (rider_onboarding)
- NAME: `Nikhil Rodrigues` (rider_onboarding)
- NAME: `D. Grewal` (rider_onboarding)
- NAME: `Bhavana Negi` (rider_onboarding)
- NAME: `Ramesh E. Bhatia` (rider_onboarding)
- NAME: `Sourav Sharma` (rider_onboarding)
- NAME: `A. Fernandes` (chat_17)
- NAME: `Harleen Sandhu` (rider_onboarding)
- NAME: `Faizan Thakur` (rider_onboarding)
- NAME: `Joseph Rathore` (rider_onboarding)
- NAME: `Sangeetha P. Agarwal` (rider_onboarding)
- NAME: `Sudha Tiwari` (rider_onboarding)
- NAME: `Gauri Kapoor` (rider_onboarding)
- PHONE: `six six eight zero six nine four eight seven seven` (chat_24)
- NAME: `Simran Jain` (rider_onboarding)
- NAME: `Yash Kulkarni` (rider_onboarding)
- NAME: `H. Iyengar` (rider_onboarding)
- NAME: `Bikash Srivastava` (rider_onboarding)
- NAME: `George D. Dutta` (rider_onboarding)
- NAME: `Deepa Khan` (rider_onboarding)
- NAME: `Padma Desai` (rider_onboarding)
- NAME: `Pranav Singh` (rider_onboarding)
- NAME: `S. Dhillon` (rider_onboarding)
- NAME: `Latha Yadav` (rider_onboarding)
- NAME: `Nikhil S. Negi` (rider_onboarding)

## Sample false alarms

- PHONE: `1800 208 9898` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `340388054019` (chat_39)
- PHONE: `1800 102 7777` (chat_39)
- PHONE: `1800 208 9898` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `530822261691` (chat_39)
- PHONE: `1800 102 7777` (chat_39)
- ADDRESS: `400028` (rider_onboarding)
- PHONE: `1800 102 7777` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `879963266438` (chat_39)
- ADDRESS: `700364` (rider_onboarding)

Gemma stats: {"calls": 435, "returned": 831, "not_in_text": 2, "bad_json": 0, "bad_label": 1}
