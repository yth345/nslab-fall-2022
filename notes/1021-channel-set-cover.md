## 1021 Channel Set Cover

- Task: Find the min channel set that can cover all edge server IPs in a day
- Dates: 2022-09-06 ~ 2022-09-07, 2022-09-11 ~ 2022-09-16

### 1. Preprocessing for optimal solution
#### (1) Process 1 (280k -> 8k)
Group channels that discovered the same set of server IPs, assigned a new group index.
#### (2) Process 2 (8k -> 0.5k)
Sort sets of IPs by their cardinality in ascending order. Starting from the smallest set, for each set S, check from the biggest set to smaller sets if S is a subset. Remove the sets of IPs that are a subset of another set.
#### (3) Result
| Date       | Init. channel count  | After process 1     | After process 2   |
| ---------- | -------------------- | ------------------- | ----------------- |
| 2022-09-06<br>H: 16-23 | 130289   | 2057 (-98.4% init.) |                   |
| 2022-09-07<br>H: 00-08 | 121650   | 1364 (-98.9% init.) |                   |
| 2022-09-11<br>H: 09-23 | 189783   | 3228 (-98.2% init.) |                   |
| 2022-09-12<br>H: 00-23 | 282847   | 7937 (-97.2% init.) | 481 (-99.8% init.)|
| 2022-09-13<br>H: 00-23 | 283392   | 11184 (-96.0% init.)| 624               |
| 2022-09-14<br>H: 00-23 | 286071   | 8184 (-97.1% init.) |                   |
| 2022-09-15<br>H: 00-23 | 283248   | 6979 (-97.5% init.) |                   |
| 2022-09-16<br>H: 00-07 | 111403   | 1304 (-98.8% init.) |                   |
