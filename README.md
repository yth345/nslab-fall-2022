# [nslab] Fall-2022 Special Topics

This is my second semester of Special Topic in NTU Network and Systems Lab aiming to exploring Twitch's CDN.

## 1. Schedule

| Date  | Assignment                                                                                                                                                         |
| ----- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 9/16  | 1. Process data in MongoDB, convert entries to same data format <br> 2. Plot daily number of unique servers found from each vantage point|
| 9/23  | compare the loss of server count when we extract probes from a country (phase 1)


## 2. Daily Unique Servers (MongoDB)

MongoDB Raw data: https://drive.google.com/drive/folders/1a4QdCcoS7G7oTThWIARGS3Heo-kF_uCJ?usp=sharing

1. All the countries have probes around April to June, 2021. (Note that in this interval, Taiwan only has a small-scale of probes at 2021-04-14 and 15.)
2. Japan, South Korea, Taiwan, Turkey, United States has additional probes in around November, 2020.

| Country         | Dates            | Number of Daily Unique Servers |
| --------------- | ---------------- | -------------------- |
| Australia       | 2021-05-06 ~ 2021-05-17 | <img src="/images/daily-servers/Australia.png" width="400"> |
| Brazil          | 2021-06-02 ~ 2021-06-15 | <img src="/images/daily-servers/Brazil.png" width="400"> |
| Canada          | 2021-06-03 ~ 2021-06-15 | <img src="/images/daily-servers/Canada.png" width="400"> |
| Denmark         | 2021-06-03 ~ 2021-06-15 | <img src="/images/daily-servers/Denmark.png" width="400"> |
| France          | 1. 2021-04-15 ~ 2021-04-24 <br> 2. 2021-04-28 ~ 2021-05-17 | <img src="/images/daily-servers/France.png" width="400"> |
| Germany         | 2021-06-03 ~ 2021-06-15 | <img src="/images/daily-servers/Germany.png" width="400"> |
| Italy           | 2021-06-02 ~ 2021-06-15 | <img src="/images/daily-servers/Italy.png" width="400"> |
| Japan           | 1. 2020-11-11, 12, 13, 15, 16 <br> 2. 2021-06-02 ~ 2021-06-15 | <img src="/images/daily-servers/Japan.png" width="400"> |
| Netherlands     | 2021-06-17 ~ 2021-07-14 | <img src="/images/daily-servers/Netherlands.png" width="400"> |
| Poland          | 2021-06-03 ~ 2021-06-14 | <img src="/images/daily-servers/Poland.png" width="400"> |
| Russian         | 2021-06-09 ~ 2021-06-15 | <img src="/images/daily-servers/Russian.png" width="400"> |
| South Korea     | 1. 2020-11-01-2020-11-10 <br> 2. 2021-04-13, 14 <br> 3. 2021-05-10 ~ 2021-05-17| <img src="/images/daily-servers/South_Korea.png" width="400"> |
| Spain           | 2021-06-02 ~ 2021-06-14 | <img src="/images/daily-servers/Spain.png" width="400"> |
| Sweden          | 2021-06-02 ~ 2021-06-15 | <img src="/images/daily-servers/Sweden.png" width="400"> |
| Taiwan          | 1. 2020-10-18 ~ 2020-11-01 <br> 2. 2020-11-17, 18, 24, 25, 26, 27 <br> 3. 2020-12-01 <br> 4. 2021-04-14, 15 | <img src="/images/daily-servers/Taiwan.png" width="400"> |
| Turkey          | 1. 2020-11-03, 04 <br> 2. 2021-06-02 ~ 2021-06-14 | <img src="/images/daily-servers/Turkey.png" width="400"> |
| Ukraine         | 2021-06-17 ~ 2021-07-14 | <img src="/images/daily-servers/Ukraine.png" width="400"> |
| United Kingdom  | 1. 2021-04-14 ~ 2021-04-24 <br> 2. 2021-04-28 ~ 2021-05-16 |  <img src="/images/daily-servers/United_Kingdom.png" width="400"> |
| United States   | 1. 2020-11-26, 27 <br> 2. 2020-11-29 ~ 2020-12-02 <br> 3. 2021-04-13 ~ 2021-04-24 <br> 4. 2021-04-28 ~ 2021-05-17|  <img src="/images/daily-servers/United_States.png" width="400"> |
