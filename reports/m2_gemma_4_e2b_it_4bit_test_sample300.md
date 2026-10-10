# gemma-4-e2b-it-4bit: data/test_sample300.jsonl

300 examples (188 chat, 112 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 42 | 42 | 100.0% | 0 | 100.0% |
| PAN | 19 | 19 | 100.0% | 0 | 100.0% |
| GSTIN | 20 | 4 | 20.0% | 0 | 100.0% |
| PHONE | 113 | 102 | 90.3% | 12 | 89.5% |
| EMAIL | 85 | 85 | 100.0% | 2 | 97.7% |
| UPI | 30 | 27 | 90.0% | 0 | 100.0% |
| CARD | 25 | 14 | 56.0% | 0 | 100.0% |
| BANK_ACCT | 18 | 0 | 0.0% | 0 | – |
| PASSPORT | 20 | 20 | 100.0% | 0 | 100.0% |
| VOTER_ID | 30 | 29 | 96.7% | 0 | 100.0% |
| VEHICLE | 70 | 35 | 50.0% | 0 | 100.0% |
| DOB | 57 | 52 | 91.2% | 0 | 100.0% |
| IP | 19 | 0 | 0.0% | 0 | – |
| **Rule labels total** | 548 | 429 | **78.3%** | 14 | **96.8%** |
| NAME | 219 | 187 | 85.4% | 0 | 100.0% |
| ADDRESS | 13 | 13 | 100.0% | 2 | 86.7% |
| DL | 0 | 0 | – | 2 | 0.0% |
| **All PII (incl. names/addresses)** | 780 | 629 | **80.6%** | 18 | |

**PII characters left visible (leak):** 17.6% overall; AADHAAR 0.0%, ADDRESS 4.1%, BANK_ACCT 100.0%, CARD 43.6%, DOB 8.5%, EMAIL 0.0%, GSTIN 80.0%, IP 100.0%, NAME 14.5%, PAN 0.0%, PASSPORT 0.0%, PHONE 11.1%, UPI 3.6%, VEHICLE 46.8%, VOTER_ID 3.3%

**Rule-label recall by source:** chat 63.3%, doc 86.8%

**Latency per message:** mean 726.175 ms · p95 1705.208 ms · p99 2136.677 ms

## Sample misses

- BANK_ACCT: `975314286` (chat_13)
- NAME: `Shalini Gill` (rider_onboarding)
- VEHICLE: `WB30ND9924` (rider_onboarding)
- IP: `203.248.151.171` (chat_20)
- NAME: `Irfan Mukherjee` (chat_17)
- NAME: `Zainab P. Gowda` (rider_onboarding)
- VEHICLE: `AP 18 VE 9843` (rider_onboarding)
- NAME: `Ramesh Mehta` (rider_onboarding)
- NAME: `Pooja Murthy` (chat_17)
- BANK_ACCT: `449007836330` (chat_13)
- GSTIN: `20PHBPF8873R1ZI` (chat_17)
- GSTIN: `11jsxpm9268l5zg` (chat_17)
- GSTIN: `16MVRPJ2478M8ZB` (chat_17)
- GSTIN: `05grips0606b8zx` (chat_17)
- BANK_ACCT: `734510115444273` (chat_13)
- GSTIN: `24NFHPD1942C9ZJ` (chat_17)
- VEHICLE: `MH 36 N 4766` (chat_19)
- BANK_ACCT: `57116734078` (chat_13)
- IP: `122.254.89.177` (chat_20)
- IP: `117.127.184.84` (chat_20)
- NAME: `Nandini Naidu` (rider_onboarding)
- VEHICLE: `KA-28-H-3994` (rider_onboarding)
- GSTIN: `21irbpc3080x6z7` (chat_17)
- BANK_ACCT: `91184504280960208` (chat_13)
- VEHICLE: `DL47VM6679` (rider_onboarding)
- VEHICLE: `AP38PD2857` (rider_onboarding)
- NAME: `Geeta Jadhav` (rider_onboarding)
- VEHICLE: `hr 34 ry 5243` (chat_19)
- VEHICLE: `GJ18MR3236` (chat_19)
- CARD: `6511-4451-1442-5628` (payment_receipt)
- IP: `122.225.13.53` (chat_20)
- VEHICLE: `TS38R7038` (chat_19)
- NAME: `h. desai` (chat_17)
- IP: `103.170.196.122` (chat_20)
- NAME: `Manoj Agarwal` (rider_onboarding)
- CARD: `4851-1645-6664-1169` (payment_receipt)
- VEHICLE: `RJ 03 G 4462` (rider_onboarding)
- NAME: `Nikhil Rodrigues` (rider_onboarding)
- IP: `106.53.86.159` (chat_20)
- BANK_ACCT: `196745591799` (chat_13)

## Sample false alarms

- PHONE: `1800 208 9898` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- DL: `DL47VM6679` (rider_onboarding)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `340388054019` (chat_39)
- PHONE: `1800 102 7777` (chat_39)
- PHONE: `1800 208 9898` (chat_39)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `530822261691` (chat_39)
- DL: `DL-58-GW-4918` (rider_onboarding)
- PHONE: `1800 102 7777` (chat_39)
- ADDRESS: `400028` (rider_onboarding)
- PHONE: `1800 102 7777` (chat_39)
- EMAIL: `swati.n88@ibl` (payment_receipt)
- PHONE: `1800-419-0505` (chat_39)
- PHONE: `879963266438` (chat_39)
- ADDRESS: `700364` (rider_onboarding)
- EMAIL: `anil.s@ibl` (payment_receipt)

Gemma stats: {"calls": 435, "returned": 831, "not_in_text": 2, "bad_json": 0, "bad_label": 1}
