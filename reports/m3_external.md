# External benchmarks: Rules + tagger
model: `models/tagger-piiranha`

## Ylemis: Latin-script slices (our scope): 5945 texts

| Group | Spans | Found (any label) | **Leak** (chars unmasked) |
|---|---|---|---|
| **gap:ALL** | 2028 | 65.9% | **55.2%** |
| gap:account_id | 1622 | 73.2% | 53.5% |
| gap:medical_id | 406 | 36.7% | 64.5% |
| **in:ALL** | 13782 | 99.2% | **0.6%** |
| in:aadhaar | 1081 | 100.0% | 0.0% |
| in:address | 1892 | 100.0% | 0.0% |
| in:email | 810 | 100.0% | 0.0% |
| in:gstin | 135 | 100.0% | 0.0% |
| in:indian_passport | 270 | 100.0% | 0.0% |
| in:indian_phone | 1758 | 100.0% | 0.0% |
| in:pan | 1621 | 100.0% | 0.0% |
| in:person | 4865 | 97.9% | 2.3% |
| in:upi_id | 675 | 100.0% | 0.0% |
| in:vehicle_registration | 405 | 100.0% | 0.0% |
| in:voter_id | 270 | 100.0% | 0.0% |

**False alarms:** 396 flagged spans overlapping no labelled entity; PII-free texts with any flag: 270/1080 (25.0%)
**Latency:** mean 27.6 ms · p95 31.4 ms

| Slice (in-scope PII) | Spans | Found | Leak |
|---|---|---|---|
| ylemis:code-mixed-IN | 675 | 100.0% | 0.0% |
| ylemis:en-IN | 10805 | 99.0% | 0.8% |
| ylemis:hi-Latn | 1082 | 100.0% | 0.0% |
| ylemis:llm-prompt-IN | 680 | 100.0% | 0.0% |
| ylemis:ocr-en-IN | 540 | 100.0% | 0.0% |

Sample false alarms:
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- NAME: `theek` (chat)
- PHONE: `9087654321` (hard_negative)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- PHONE: `9087654321` (hard_negative)
- NAME: `theek` (chat)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- ADDRESS: `warehouse bay 12, lot 3308` (hard_negative)
- NAME: `theek` (chat)

## Ylemis: native-script slices (out of scope): 4055 texts

| Group | Spans | Found (any label) | **Leak** (chars unmasked) |
|---|---|---|---|
| **gap:ALL** | 1081 | 80.5% | **40.8%** |
| gap:account_id | 811 | 93.7% | 35.6% |
| gap:medical_id | 270 | 40.7% | 62.7% |
| **in:ALL** | 10137 | 99.7% | **0.4%** |
| in:aadhaar | 676 | 100.0% | 0.0% |
| in:address | 1757 | 99.4% | 0.6% |
| in:email | 270 | 100.0% | 0.0% |
| in:gstin | 270 | 100.0% | 0.0% |
| in:indian_passport | 135 | 99.3% | 0.7% |
| in:indian_phone | 1892 | 100.0% | 0.0% |
| in:pan | 946 | 100.0% | 0.0% |
| in:person | 3379 | 100.0% | 0.0% |
| in:upi_id | 406 | 100.0% | 0.0% |
| in:vehicle_registration | 135 | 100.0% | 0.0% |
| in:voter_id | 271 | 94.8% | 8.3% |

**False alarms:** 136 flagged spans overlapping no labelled entity; PII-free texts with any flag: 136/676 (20.1%)
**Latency:** mean 27.8 ms · p95 31.6 ms

| Slice (in-scope PII) | Spans | Found | Leak |
|---|---|---|---|
| ylemis:bn | 1629 | 99.1% | 1.6% |
| ylemis:gu | 540 | 100.0% | 0.0% |
| ylemis:hi | 3375 | 99.7% | 0.3% |
| ylemis:kn | 405 | 100.0% | 0.0% |
| ylemis:mixed-script-IN | 945 | 99.9% | 0.1% |
| ylemis:mr | 540 | 100.0% | 0.0% |
| ylemis:pa | 405 | 100.0% | 0.0% |
| ylemis:ta | 1758 | 99.9% | 0.1% |
| ylemis:te | 540 | 100.0% | 0.0% |

Sample false alarms:
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)
- BANK_ACCT: `5566778` (hard_negative)

## Maskara real_world_eval (en-IN): 2600 texts

| Group | Spans | Found (any label) | **Leak** (chars unmasked) |
|---|---|---|---|
| **gap:ALL** | 400 | 51.0% | **77.0%** |
| gap:API_KEY | 200 | 17.0% | 93.4% |
| gap:USERNAME | 200 | 85.0% | 15.5% |
| in:AADHAAR | 1000 | 96.5% | 3.7% |
| in:ADDRESS | 400 | 100.0% | 2.5% |
| **in:ALL** | 7200 | 99.4% | **2.1%** |
| in:DATE_OF_BIRTH | 200 | 100.0% | 5.1% |
| in:DRIVER_LICENSE | 200 | 100.0% | 5.9% |
| in:EMAIL | 700 | 100.0% | 0.0% |
| in:IP_ADDRESS | 200 | 100.0% | 3.1% |
| in:PAN_CARD | 400 | 99.8% | 0.2% |
| in:PERSON_NAME | 2200 | 100.0% | 0.0% |
| in:PHONE | 1200 | 100.0% | 5.9% |
| in:UPI_ID | 500 | 100.0% | 0.0% |
| in:VEHICLE_REG | 200 | 98.0% | 9.3% |

**False alarms:** 286 flagged spans overlapping no labelled entity; PII-free texts with any flag: 65/200 (32.5%)
**Latency:** mean 29.7 ms · p95 35.4 ms

| Slice (in-scope PII) | Spans | Found | Leak |
|---|---|---|---|
| maskara_real:api_request | 600 | 100.0% | 2.3% |
| maskara_real:bank_statement | 600 | 96.0% | 3.5% |
| maskara_real:email | 800 | 100.0% | 1.7% |
| maskara_real:govt_form | 1400 | 99.9% | 1.5% |
| maskara_real:json | 800 | 98.6% | 2.6% |
| maskara_real:log | 200 | 100.0% | 3.1% |
| maskara_real:ocr | 400 | 100.0% | 0.1% |
| maskara_real:support_ticket | 900 | 100.0% | 1.6% |
| maskara_real:transport | 600 | 99.3% | 5.1% |
| maskara_real:whatsapp | 900 | 100.0% | 1.7% |

Sample false alarms:
- ADDRESS: `Flat 260, 7th Floor, Gachibowli, Mahatma Gandhi Road, Faridabad - 635565` (hard)
- NAME: `Pimpri` (hard_negative)
- ADDRESS: `802/7, Phase 2,
Lajpat Nagar,
Kalyan, Tripura - 726847` (hard)
- ADDRESS: `dabad` (hard_negative)
- ADDRESS: `Jawaharlal Nehru Road, near bus stand, Madurai 094282` (hard)
- PHONE: `754621997528` (hard_negative)
- ADDRESS: `793/15, Whitefield,
Sardar Patel Marg,
Visakhapatnam, Tripura - 760346` (hard)
- PHONE: `614363976859` (hard_negative)
- ADDRESS: `Marine Drive, behind railway station, Kalyan, Karnataka - 427513` (hard)
- ADDRESS: `Village Ayush, Post Ahmedabad, Tehsil Thane, District Kolkata, West Bengal` (hard)
- ADDRESS: `Bhagat Singh Road, beside mosque, Agra 472040` (hard)
- ADDRESS: `FC Road, near temple, Navi Mumbai 947861` (hard)
- ADDRESS: `P.O. Box 4830, Nagpur - 274941` (hard)
- ADDRESS: `P.O. Box 1862, Thiruvananthapuram - 455665` (hard)
- ADDRESS: `Netaji Subhas Road, beside ICICI Bank, Pune, West Bengal - 250547` (hard)
- ADDRESS: `P.O. Box 8491, Delhi - 019786` (hard)
- ADDRESS: `Flat 458, 8th Floor, Dwarka, Indira Gandhi Road, Tiruppur - 885752` (hard)
- ADDRESS: `Netaji Subhas Road, in front of Big Bazaar, Vijayawada, Himachal Pradesh - 160969` (hard)
- ADDRESS: `240/5, Aundh,
Ambedkar Nagar,
Vijayawada, Meghalaya - 714383` (hard)
- ADDRESS: `gaon` (hard_negative)
- NAME: `lan` (medium)
- ADDRESS: `P.O. Box 8379, Jabalpur - 799118` (hard)
- PHONE: `891862163703` (hard_negative)
- ADDRESS: `sore` (hard_negative)
- PHONE: `858222169919` (hard_negative)

## Maskara template_disjoint_eval (en-IN + hi-IN): 10457 texts

| Group | Spans | Found (any label) | **Leak** (chars unmasked) |
|---|---|---|---|
| **gap:ALL** | 2122 | 49.1% | **71.1%** |
| gap:API_KEY | 743 | 2.6% | 99.0% |
| gap:PASSWORD | 665 | 71.3% | 21.4% |
| gap:USERNAME | 714 | 76.8% | 23.8% |
| in:AADHAAR | 2866 | 96.3% | 5.0% |
| in:ADDRESS | 1695 | 99.8% | 2.4% |
| **in:ALL** | 24523 | 98.2% | **4.6%** |
| in:CREDIT_CARD | 487 | 71.0% | 31.3% |
| in:DATE_OF_BIRTH | 1734 | 99.0% | 6.6% |
| in:DRIVER_LICENSE | 971 | 100.0% | 7.3% |
| in:EMAIL | 2128 | 100.0% | 0.1% |
| in:IP_ADDRESS | 746 | 100.0% | 3.8% |
| in:PAN_CARD | 582 | 89.9% | 11.2% |
| in:PASSPORT | 622 | 91.5% | 9.0% |
| in:PERSON_NAME | 6126 | 99.7% | 0.6% |
| in:PHONE | 4938 | 99.6% | 9.7% |
| in:UPI_ID | 674 | 100.0% | 0.0% |
| in:VEHICLE_REG | 954 | 97.6% | 10.0% |

**False alarms:** 105 flagged spans overlapping no labelled entity; PII-free texts with any flag: 0/0 (–)
**Latency:** mean 28.0 ms · p95 35.2 ms

| Slice (in-scope PII) | Spans | Found | Leak |
|---|---|---|---|
| maskara_disjoint:aadhaar_letter | 216 | 99.5% | 1.5% |
| maskara_disjoint:api_request | 2220 | 100.0% | 2.0% |
| maskara_disjoint:bank_statement | 186 | 97.3% | 2.9% |
| maskara_disjoint:chat_prompt | 132 | 100.0% | 2.4% |
| maskara_disjoint:config | 430 | 100.0% | 4.0% |
| maskara_disjoint:contact_management | 2140 | 96.6% | 5.3% |
| maskara_disjoint:csv | 141 | 95.0% | 6.5% |
| maskara_disjoint:email | 244 | 100.0% | 2.3% |
| maskara_disjoint:finance | 900 | 89.3% | 12.9% |
| maskara_disjoint:govt_form | 1756 | 100.0% | 2.3% |
| maskara_disjoint:html | 2151 | 100.0% | 1.6% |
| maskara_disjoint:identity | 2163 | 92.8% | 9.3% |
| maskara_disjoint:json | 3004 | 99.9% | 1.6% |
| maskara_disjoint:log | 54 | 100.0% | 2.7% |
| maskara_disjoint:markdown | 177 | 100.0% | 2.4% |
| maskara_disjoint:ocr | 112 | 100.0% | 0.0% |
| maskara_disjoint:pan_doc | 153 | 98.0% | 4.3% |
| maskara_disjoint:resume | 228 | 96.5% | 6.9% |
| maskara_disjoint:sms | 1242 | 97.4% | 18.8% |
| maskara_disjoint:sql | 300 | 91.7% | 12.0% |
| maskara_disjoint:support_ticket | 3284 | 100.0% | 2.2% |
| maskara_disjoint:transport | 2912 | 99.4% | 6.3% |
| maskara_disjoint:whatsapp | 378 | 95.5% | 7.8% |

Sample false alarms:
- NAME: `Challan` (medium)
- PHONE: `+918295379298` (medium)
- PHONE: `9078274653` (medium)
- EMAIL: `mangesh.s@yahoo.com` (medium)
- EMAIL: `prachi.t@hotmail.com` (medium)
- NAME: `Harsha Kashyap` (medium)
- PHONE: `58305 83277` (medium)
- NAME: `Bhargav K` (medium)
- PHONE: `3953276052` (medium)
- PHONE: `022 09061338` (medium)
- EMAIL: `mrs..meena.bhatia751@example.com` (medium)
- PHONE: `9112988372` (medium)
- PHONE: `0033-0374-5776` (medium)
- PHONE: `+91-66590-00539` (medium)
- EMAIL: `chandra.gulati@gmail.com` (medium)
- PHONE: `6394346225` (medium)
- PHONE: `+91-66532-84358` (medium)
- EMAIL: `jayesh.dayal@icloud.com` (medium)
- PHONE: `+910899473773` (medium)
- EMAIL: `lakshmi.h@live.in` (medium)
- PHONE: `+91) 28518 31229` (medium)
- EMAIL: `mahesh.d561@hotmail.com` (medium)
- PHONE: `+91 46704 76590` (medium)
- EMAIL: `nikhil.r370@gmail.com` (medium)
- PHONE: `08881644293` (medium)

