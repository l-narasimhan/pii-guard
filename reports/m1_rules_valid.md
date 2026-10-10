# Rule layer: data/valid.jsonl

1000 examples (603 chat, 397 doc)

| Label | Real spans | Found | Recall | False alarms | Precision |
|---|---|---|---|---|---|
| AADHAAR | 89 | 89 | 100.0% | 0 | 100.0% |
| PAN | 97 | 97 | 100.0% | 0 | 100.0% |
| GSTIN | 172 | 172 | 100.0% | 0 | 100.0% |
| PHONE | 480 | 464 | 96.7% | 0 | 100.0% |
| EMAIL | 246 | 246 | 100.0% | 0 | 100.0% |
| UPI | 62 | 62 | 100.0% | 0 | 100.0% |
| CARD | 45 | 45 | 100.0% | 0 | 100.0% |
| BANK_ACCT | 81 | 81 | 100.0% | 0 | 100.0% |
| PASSPORT | 22 | 22 | 100.0% | 0 | 100.0% |
| VOTER_ID | 26 | 26 | 100.0% | 0 | 100.0% |
| VEHICLE | 48 | 48 | 100.0% | 0 | 100.0% |
| DOB | 60 | 60 | 100.0% | 0 | 100.0% |
| IP | 62 | 62 | 100.0% | 0 | 100.0% |
| **Rule labels total** | 1490 | 1474 | **98.9%** | 0 | **100.0%** |
| NAME | 798 | 0 | 0.0% | 0 | – |
| ADDRESS | 403 | 0 | 0.0% | 0 | – |
| **All PII (incl. names/addresses)** | 2691 | 1474 | **54.8%** | 0 | |

**Rule-label recall by source:** chat 98.4%, doc 99.1%

**Latency per message:** mean 0.043 ms · p95 0.097 ms · p99 0.115 ms

## Sample misses (rule labels)

- PHONE: `72231 44305` (app_log)
- PHONE: `6707 558 385` (app_log)
- PHONE: `8317096231` (app_log)
- PHONE: `09425062575` (app_log)
- PHONE: `nine two two four four six eight six nine six` (chat_5)
- PHONE: `+91-9818063326` (app_log)
- PHONE: `six two seven zero three four six four seven zero` (chat_21)
- PHONE: `nine nine nine nine two zero five one four three` (chat_21)
- PHONE: `+919576173498` (app_log)
- PHONE: `60280 71836` (app_log)
- PHONE: `06697910863` (app_log)
- PHONE: `8322140845` (app_log)
- PHONE: `+91 66941 88813` (app_log)
- PHONE: `six seven three two six seven seven eight four eight` (chat_12)
- PHONE: `nine eight zero zero nine seven six seven five seven` (chat_46)

## Sample false alarms

- none
