| Concurrent clients | Messages/sec | p50 ms | p95 ms | p99 ms | Errors |
|---|---|---|---|---|---|
| 1 | 54 | 18.7 | 30.2 | 35.6 | 0 |
| 4 | 67 | 59.0 | 75.7 | 86.0 | 0 |
| 8 | 71 | 113.0 | 135.9 | 149.3 | 0 |
| 16 | 75 | 215.7 | 246.0 | 268.1 | 0 |

| Steady arrival rate | Messages | p50 ms | p95 ms | p99 ms | Errors |
|---|---|---|---|---|---|
| 10 msg/s steady | 200 | 18.2 | 29.8 | 35.4 | 0 |
| 30 msg/s steady | 600 | 10.4 | 19.4 | 21.3 | 0 |
| 50 msg/s steady | 1000 | 10.5 | 19.4 | 23.3 | 0 |
