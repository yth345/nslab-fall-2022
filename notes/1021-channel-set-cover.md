## 1021 Channel Set Cover

- Task: Find the min channel set that can cover all edge server IPs in a day
- Dates: 2022-09-06 ~ 2022-09-07, 2022-09-11 ~ 2022-09-16
- Probing location: NSLab (Taiwan)

### 1. Preprocessing Steps
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
| 2022-09-13<br>H: 00-23 | 283392   | 11184 (-96.0% init.)| 624 (-99.8% init.)|
| 2022-09-14<br>H: 00-23 | 286071   | 8184 (-97.1% init.) |                   |
| 2022-09-15<br>H: 00-23 | 283248   | 6979 (-97.5% init.) |                   |
| 2022-09-16<br>H: 00-07 | 111403   | 1304 (-98.8% init.) |                   |  


### 2. Greedy Approximate (at 2022-09-12)
There are multiple sets that has the maximum cardinality (= 20), try starting with selecting each of the sets.  
For each round, pick the set that has the most uncovered IPs.  
Result: 22 channels can cover 49 IPs found at 2022-09-12.
```
num of IPs in 2022-09-12: 49
1.
uncoverd IP cnt: 49 29 26 23 21 19 17 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 1: 22 channels
2.
uncoverd IP cnt: 49 29 25 22 20 18 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 2: 22 channels
3.
uncoverd IP cnt: 49 29 26 23 20 18 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 3: 22 channels
4.
uncoverd IP cnt: 49 29 25 22 20 18 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 4: 22 channels
5.
uncoverd IP cnt: 49 29 26 23 20 18 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 5: 22 channels
6.
uncoverd IP cnt: 49 29 25 22 20 18 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0
approximate solution 6: 22 channels
```

### 3. Approximate Ratio and Optimal Solution
Let $X$ be the set of all server IPs we discovered in a day,  
$F$ be the set of subsets of $X$, which is a collection of the sets we get after process 2.

Greedy algorithm is a polynomial-time $\alpha$-approximation algorithm, where  
$$\alpha = H(\max \set{ |S|: S \in F } )$$ and $H(n) = \Sigma_{i=1}^{n} \frac{1}{n} \le \log n + 1$.  

The maximum cardinality of subsets is $20$ at 2022-09-12,  
$H(20) \le \log 20 + 1 = 2.3$,  
the approximate solution we get is $22$ channels,  
$22 \div 2.3 = 9.57$,  
thus, the optimal solution could be as good as $10$ channels.

#### Summary:
| Date       | Subset count | Num of IPs | Apprx. set cover | Optimal set cover |
| ---------- | ------------ | ---------- | ---------------- | ----------------- |
| 2022-09-12 | 481          | 49         | 22 channels      | 10 ~ 22 channels  |
