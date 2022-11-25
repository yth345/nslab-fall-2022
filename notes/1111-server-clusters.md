## 1111 Server Clusters
- Dates: 2022-09-06 ~ 2022-09-07, 2022-09-11 ~ 2022-09-16
- Probing Location: NSLab (Taiwan)

### 1. Server Overview
| IP set            | # of IPs | Visible time  | IP Location (ISP)  | IATA code | channel langauge | # of unique channels |
| ----------------- | -------- | ------------- | ------------------ | --------- | ---------------- | -------------------- |
| 99.181.91.*       | 21       | always        | San Francisco <br>(twitch.tv)  | HKG | all        | 743175       |
| 99.181.106/107.*  | 15       | 09/11 (H: 14, 15, 16), <br>09/12 (H: 14, 15), <br>09/13 (H: 11, 13~17), <br>09/14 (H: 13, 14, 15), <br>09/15 (H: 14)| San Francisco <br>(twitch.tv)  | SJC | Asian, European | 91602 |
| 45.113.129/130.*  | 55       | 09/06 (H: 19, 20), <br>09/11 (H: 16~20), <br>09/12 (H: 19), <br>09/13 (H: 09, 22, 23), <br>09/15 (H: 08, 21)| Hong Kong <br>(twitch.tv) | TPE | European, American, <br>a few Arabian | 651 |
| 52.223.247.* <br> (AWS IP)     | 31       | 09/06 (H: 15) | San Francisco <br>(twitch.tv) | LAX | mainly Asian, English | 137          |
| 163.28.5.33       | 1        | 09/16 (H: 02) | Taipei <br>(TANet)  | - | - | 1   |

### 2. Channel Selecting Criteria
__(1) Group 99.181.91.\* -- select from highest viewer count__   
  - Consider the dates that we probed all day long, for each hour, selecting the top 0.28% of channels can cover all IPs in this group.  
  - Consider all the dates (excluding those we didn't probe full hour), for each hour, selecting top 0.90% of channels can cover all IPs in this group.
  - Possible criteria: Select from the highest viewer count channel until we select 2% of channels seen in that hour.

__(2) Group 99.181.106/107.*__ 
  - If we select from __highest viewer count__, we have to select up to 57% of channels in an hour, the bottleneck appears at 2022-09-11T14 (select up to 57%) and 2022-09-12T16 (select up to 52%). The discription of IPs found at the two hour is at __3. Appendix__.  
  - If we try to select __specific hours__ throughout each dates to form a server cover, we see that selecting either hour of `11, 13~17` is okay.  
  
  Total number of unique cluster 2 IPs we see across the dates is 15.
  | hour | # of unique cluster 2 IPs seen in hour |
  | ---- | -------------------------------------- |
  | 11 | 15 | 
  | 13 | 15 | 
  | 14 | 15 |
  | 15 | 15 | 
  | 16 | 15 |
  | 17 | 15 |

__(3) Group 45.113.129/130.*__ 
  - If we select from __highest viewer count__, the amount of channels we have to select are generally high, the highest is 96% of channels at 2022-09-11T18.
  - If we try to select __specific hours__ throughout each dates to form a server cover, selecting hours `19, 20, 09, 17` can form a min set cover.  

  Total number of unique cluster 3 IPs we see across the dates is 55.
  | hour | # of unique cluster 3 IPs seen in hour |
  | ---- | -------------------------------------- |
  | 08 |  1 |
  | 09 | 28 |
  | 16 | 23 |
  | 17 | 11 |
  | 18 |  9 |
  | 19 | 48 |
  | 20 | 24 |
  | 21 |  2 |
  | 22 |  1 |
  | 23 |  2 |
  
__(4) Group 52.223.247.*__ 
  - If we select from highest viewer count, we need to select up to 19% of channels.

__(5) Group 163.28.5.33__ 
  - This IP should be a mistake from recording the probes.


### 3. Appendix
#### (1) Cluster 2 bottleneck hours
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
