# Rule layer: data/test.jsonl

1500 examples (911 chat, 589 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 241 | 241 | 100.0% | 0 | 100.0% |
| PAN | 96 | 96 | 100.0% | 0 | 100.0% |
| GSTIN | 76 | 76 | 100.0% | 0 | 100.0% |
| PHONE | 593 | 586 | 98.8% | 0 | 100.0% |
| EMAIL | 414 | 414 | 100.0% | 0 | 100.0% |
| UPI | 179 | 179 | 100.0% | 0 | 100.0% |
| CARD | 189 | 189 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 79 | 79 | 100.0% | 0 | 100.0% |
| PASSPORT | 65 | 65 | 100.0% | 0 | 100.0% |
| VOTER_ID | 164 | 164 | 100.0% | 0 | 100.0% |
| VEHICLE | 356 | 356 | 100.0% | 0 | 100.0% |
| DOB | 286 | 286 | 100.0% | 0 | 100.0% |
| IP | 78 | 78 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 2816 | 2809 | **99.8%** | 0 | **100.0%** |
| NAME | 1121 | 0 | 0.0% | 0 | – |
| ADDRESS | 83 | 0 | 0.0% | 0 | – |
| **All PII (incl. names/addresses)** | 4020 | 2809 | **69.9%** | 0 | |

**Rule-label recall by source:** chat 99.2%, doc 100.0%

**Latency per message:** mean 0.033 ms · p95 0.059 ms · p99 0.067 ms

## Sample misses

- NAME: `Yogesh Iyer` (payment_receipt)
- NAME: `Prakash Desai` (chat_19)
- NAME: `Irfan Nair` (payment_receipt)
- NAME: `ishita khanna` (chat_13)
- NAME: `Pooja Fernandes` (payment_receipt)
- NAME: `simran tiwari` (chat_24)
- NAME: `K. Murthy` (chat_19)
- NAME: `Revathi Pillai` (chat_17)
- NAME: `shanti pereira` (chat_44)
- NAME: `Nikhil B. Agarwal` (rider_onboarding)
- NAME: `Rekha Shastri` (chat_17)
- NAME: `Latha Sethi` (rider_onboarding)
- NAME: `Ramesh Mehta` (rider_onboarding)
- NAME: `Jasvinder Yadav` (chat_24)
- NAME: `mary sethi` (chat_44)
- ADDRESS: `c-1526, raheja vihar, sector 62` (chat_9)
- NAME: `Imran Sethi` (payment_receipt)
- ADDRESS: `Shanti Kunj Apartments, flat E-1822, beside St. Mary's church, Mansarovar 302089` (chat_9)
- NAME: `Nikhil Gill` (rider_onboarding)
- NAME: `Ramesh Patil` (rider_onboarding)
- NAME: `Naveen D. Mukherjee` (chat_44)
- NAME: `Chitra Subramanian` (chat_13)
- NAME: `Anjali Jain` (payment_receipt)
- NAME: `Salman Verma` (rider_onboarding)
- NAME: `Prakash Malhotra` (rider_onboarding)
- NAME: `Priya B. Jain` (payment_receipt)
- NAME: `Manoj Thomas` (chat_19)
- NAME: `Meera Khan` (payment_receipt)
- NAME: `Durga Dutta` (chat_19)
- NAME: `Uma Yadav` (payment_receipt)
- NAME: `Asha Krishnan` (payment_receipt)
- NAME: `Shanti Rathore` (rider_onboarding)
- NAME: `n. banerjee` (chat_44)
- NAME: `Salman H. Shah` (rider_onboarding)
- NAME: `Balaji E. Sethi` (rider_onboarding)
- NAME: `Yash Kamath` (rider_onboarding)
- NAME: `Nandini Roy` (rider_onboarding)
- ADDRESS: `shanti kunj apartments, flat c-175, near bus stand, sector 137 201984` (chat_9)
- NAME: `Pranav Agarwal` (payment_receipt)
- NAME: `M. Saxena` (rider_onboarding)

## Sample false alarms

- none
