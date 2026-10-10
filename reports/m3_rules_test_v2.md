# Rule layer: data/test.jsonl

2000 examples (1191 chat, 809 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 198 | 198 | 100.0% | 0 | 100.0% |
| PAN | 91 | 50 | 54.9% | 0 | 100.0% |
| GSTIN | 36 | 36 | 100.0% | 0 | 100.0% |
| PHONE | 1680 | 1561 | 92.9% | 0 | 100.0% |
| EMAIL | 338 | 305 | 90.2% | 0 | 100.0% |
| UPI | 211 | 174 | 82.5% | 0 | 100.0% |
| CARD | 162 | 162 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 39 | 39 | 100.0% | 0 | 100.0% |
| PASSPORT | 45 | 45 | 100.0% | 0 | 100.0% |
| VOTER_ID | 165 | 165 | 100.0% | 0 | 100.0% |
| VEHICLE | 313 | 313 | 100.0% | 0 | 100.0% |
| DOB | 276 | 276 | 100.0% | 0 | 100.0% |
| IP | 40 | 40 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 3594 | 3364 | **93.6%** | 0 | **100.0%** |
| NAME | 2044 | 0 | 0.0% | 0 | – |
| ADDRESS | 129 | 0 | 0.0% | 0 | – |
| DL | 40 | 40 | 100.0% | 0 | 100.0% |
| **All PII (incl. names/addresses)** | 5807 | 3404 | **58.6%** | 0 | |

**PII characters left visible (leak):** 42.5% overall; AADHAAR 0.0%, ADDRESS 100.0%, BANK_ACCT 0.0%, CARD 0.0%, DL 0.0%, DOB 0.0%, EMAIL 10.6%, GSTIN 0.0%, IP 0.0%, NAME 100.0%, PAN 46.7%, PASSPORT 0.0%, PHONE 6.4%, UPI 15.9%, VEHICLE 0.0%, VOTER_ID 0.0%

**Rule-label recall by source:** chat 72.9%, doc 100.0%

**Latency per message:** mean 0.037 ms · p95 0.079 ms · p99 0.097 ms

## Sample misses

- PHONE: `+966 50 191 8436` (chat_77)
- NAME: `Karthik Bhatia` (visitor_log)
- NAME: `Bharati Mahajan` (visitor_log)
- NAME: `Manoj Fernandes` (visitor_log)
- NAME: `Ramesh K. Gill` (visitor_log)
- ADDRESS: `D-1878, Green Valley Apartments, Adyar` (chat_9)
- NAME: `Pranav S. Krishnan` (chat_65)
- NAME: `Vikram Kulkarni` (chat_44)
- ADDRESS: `opp Sri Sai bakery, brown building 5th floor, Kaloor` (chat_90)
- ADDRESS: `gali no 8, church ke peeche, Kakkanad` (chat_90)
- PHONE: `+966 53 231 9007` (chat_77)
- NAME: `sanjay` (chat_54)
- ADDRESS: `house with yellow gate near sbi atm, gachibowli` (chat_66)
- NAME: `rohit` (chat_66)
- NAME: `Meenakshi Kulkarni` (visitor_log)
- NAME: `Joseph S. Deshpande` (visitor_log)
- NAME: `Gurpreet Shah` (visitor_log)
- NAME: `S. Menon` (visitor_log)
- NAME: `Tanvi Tiwari` (visitor_log)
- NAME: `Rohit Thakur` (rider_onboarding)
- NAME: `S. Kamath` (rider_onboarding)
- ADDRESS: `Ayyappa temple pakkam, 13th street, Navrangpura, Ahmedabad` (chat_90)
- NAME: `Suresh Sayyed` (payment_receipt)
- NAME: `Parvati N. Patil` (chat_19)
- NAME: `Pooja Sharma` (rider_onboarding)
- NAME: `Kiran G. Sayyed` (rider_onboarding)
- NAME: `Pooja` (chat_50)
- NAME: `S. Goyal` (rider_onboarding)
- NAME: `Pradeep Mehta` (rider_onboarding)
- NAME: `Teresa Dhillon` (visitor_log)
- NAME: `George Ghosh` (visitor_log)
- NAME: `Abdul T. Patil` (visitor_log)
- PHONE: `60598` (chat_71)
- ADDRESS: `flat d-984, raheja vihar, near water tank, navrangpura, ahmedabad - 380370` (chat_9)
- UPI: `manpreet@cnrb` (chat_83)
- NAME: `P. Thakur` (visitor_log)
- NAME: `Padma Fernandes` (visitor_log)
- NAME: `Arjun Rao` (visitor_log)
- NAME: `Tanmoy Chatterjee` (rider_onboarding)
- NAME: `Radha Pereira` (rider_onboarding)

## Sample false alarms

- none
