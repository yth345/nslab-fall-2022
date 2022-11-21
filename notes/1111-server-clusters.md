## 1111 Server Clusters
- Dates: 2022-09-06 ~ 2022-09-07, 2022-09-11 ~ 2022-09-16
- Probing Location: NSLab (Taiwan)

### 1. Server Overview
| IP set            | # of IPs | Visible time  | IP Location (ISP)  | IATA code | # of unique channels |
| ----------------- | -------- | ------------- | ------------------ | --------- | -------------------- |
| 99.181.91.*       | 21       | always        | San Francisco (twitch.tv)  | HKG | 743175       |
| 99.181.106/107.*  | 15       | 2022-09-11(T14, T15, T16), <br>2022-09-12(T14, T15), <br>2022-09-13(T11, T13~17, T22, T23), <br>2022-09-14(T13, T14, T15), <br>2022-09-15(T14)| San Francisco (twitch.tv)  | SJC | 91602 |
| 45.113.129/130.*  | 55       | 2022-09-06(T19, T20), <br>2022-09-11(T16~20), <br>2022-09-12 (T19), <br>2022-09-13 (T09), <br>2022-09-15(T08, T21)| Hong Kong (twitch.tv) | TPE |  651 |
| 52.223.247.*      | 31       | 2022-09-06(T15) | San Francisco (twitch.tv) | LAX | 137          |
| 163.28.5.33       | 1        | 2022-09-16(T02) | Taipei (Taiwan Academic Network)  | - | 1   |

### 2. Channel Selecting Criteria
__(1) Group 99.181.91.\* -- select from highest viewer count__   
  - Consider the dates that we probed all day long, for each hour, selecting the top 0.28% of channels can cover all IPs in this group.  
  - Consider all the dates (excluding those we didn't probe full hour), for each hour, selecting top 0.90% of channels can cover all IPs in this group.
  - Possible criteria: Select from the highest viewer count channel until we select 3% of channels seen in that hour.

__(2) Group 99.181.106/107.*__ 
  - If we select from highest viewer count, we have to select up to 57% of channels in an hour, the bottleneck appears at 2022-09-11T14 (select up to 57%) and 2022-09-12T16 (select up to 52%).  

2022-09-11T14:
| server_ip      | channel_cnt | language     | cumu_viewer_cnt |
| -------------- | ----------- | ------------ | --------------- |
| 99.181.106.228 | 2           | {'ko'}       | 284            |
| 99.181.106.246 | 1           | {'ko'}       | 101            |
| 99.181.107.16  | 2           | {'ko', 'zh'} | 546            |
| 99.181.107.36  | 2           | {'ko'}       | 124            |
| 99.181.107.38  | 2           | {'en', 'zh'} | 150            |
| 99.181.107.39  | 1           | {'ko'}       | 68             |
| 99.181.107.5   | 1           | {'ko'}       | 15             |
| 99.181.107.6   | 3           | {'en', 'ja'} | 112            |
| 99.181.107.69  | 1           | {'zh'}       | 92             |
| 99.181.107.80  | 2           | {'ko', 'zh'} | 328            |
| 99.181.107.87  | 1           | {'ja'}       | 13             |

2022-09-12T16:
|server_ip     |channel_cnt|language    |cumu_viewer_cnt|
|--------------|-----------|------------|---------------|
|99.181.106.247|2          |{'en'}      |25             |

__(3) Group 45.113.129/130.*__ 
  - If we select from highest viewer count, the amount of channels we have to select are generally high, the highest is 96% of channels at 2022-09-11T18.

__(4) Group 52.223.247.*__ 
  - If we select from highest viewer count, we need to select up to 19% of channels.

__(5) Group 163.28.5.33__ 
  - This IP should be a mistake from recording the probes.
