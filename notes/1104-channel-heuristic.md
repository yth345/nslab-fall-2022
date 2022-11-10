## 1104 Heuristic Algorithms for Channel Set Cover
- Date: 2022-09-12
- Probing Location: NSLab (Taiwan)

### 1. Data Analysis
#### (1) Twitch stream info
Stream information returned from Twitch's API included the following:  
```
id, user_id, user_login, user_name, 
game_id, game_name, 
type, title, viewer_count, started_at, language, thumbnail_url, tag_ids, is_mature
```
The entries we find relevant to our purpose are: `viewer_count`, `langauge`

#### (2) Top 26 languages with the max IPs found in a channel (at 2022-09-12)
Note: If the maximium number of IPs found in a channel in a specific language is the same, order by the average IPs found.
|     | Languages                  | Channel count | Max IP count | Avg. IP count |
| --- | -------------------------- | ------------- | ------------ | ------------- |
| 1   | en (English)               | 462384        | 19           | 1.06          |
| 2   | zh-hk (Chinese (Hong Kong))| 1872          | 18           | 1.22          |
| 3   | th (Thai)                  | 6367          | 10           | 1.46          |
| 4   | zh (Chinese)               | 19284         | 9            | 1.18          |
| 5   | fi (Finnish)               | 2555          | 8            | 1.11          |
| 6   | ko (Korean)                | 49535         | 8            | 1.10          |
| 7   | ru (Russian)               | 48187         | 8            | 1.08          |
| 8   | ja (Japanese)              | 38466         | 7            | 1.09          |
| 9   | tr (Turkish)               | 10522         | 7            | 1.07          |
| 10  | pt (Portuguese)            | 55145         | 7            | 1.07          |
| 11  | de (German)                | 53440         | 7            | 1.07          |
| 12  | fr (French)                | 47626         | 6            | 1.07          |
| 13  | es (Spanish)               | 102194        | 6            | 1.06          |
| 14  | id (Indonesian)            | 776           | 5            | 1.12          |
| 15  | hu (Hungarian)             | 2989          | 5            | 1.09          |
| 16  | it (Italian)               | 15872         | 5            | 1.08          |
| 17  | tl (Tagalog)               | 713           | 4            | 1.13          |
| 18  | other                      | 2523          | 4            | 1.09          |
| 19  | bg (Bulgarian)             | 1192          | 4            | 1.09          |
| 20  | da (Danish)                | 1438          | 4            | 1.08          |
| 21  | ar (Arabic)                | 8247          | 4            | 1.08          |
| 22  | el (Greek)                 | 1348          | 4            | 1.08          |
| 23  | uk (Ukrainian)             | 1428          | 4            | 1.08          |
| 24  | pl (Polish)                | 9226          | 4            | 1.08          |
| 25  | no (Norwegian)             | 1092          | 4            | 1.07          |
| 26  | sv (Swedish)               | 1981          | 4            | 1.07          |


### 2. Algorithms
Since we cannot know the number of servers serving each channel at the time we get a list of stream info, we must develop a heuristic to reduce the channel amount we plan to probe.  

We compare the following algorithms that finds a channel set cover:  
- **Greedy:** Select the channel that can cover the most uncovered server IPs, repeat until we reach set cover.  
- **Heuristic:** Select the channel with the most viewer count each round, repeat until we reach set cover.  

#### (1) Result
We can see that greedy and heuristic algorithm both performs well on reducing the number of channels that we need to probe, except for heuristic algorithm on hour 16 and hour 19.  
<img src="/images/channel-1.png" width="600">

If we take a look at what happend in the two hours, we found that some servers appear only in channels that have a few viewers.  

**a. 2022-09-12T16**
|    | IP              | User Login        | IPs discoverd from the channel   | language | viewer count |
| -- | --------------- | ----------------- | -------------------------------- | -------- | ------------ |
| 1  | 99.181.106.247  | royex             | '99.181.106.247', '99.181.91.31' | en       | 20           |
|    |                 | skimbyp           | '99.181.106.247'                 | en       | 5            |

**b. 2022-09-12T19**
|    | IP              | User Login        | IPs discoverd from the channel   | language | viewer count |
| -- | --------------- | ----------------- | -------------------------------- | -------- | ------------ |
| 1  | 45.113.129.141  | laurelinx_        | '99.181.91.58', '45.113.129.141' | fr       | 43           |
|    |                 | pixel_drops       | '99.181.91.16', '45.113.129.141' | en       | 5            |
| 2  | 45.113.129.142  | carlyboo1992      | '99.181.91.28', '45.113.129.142' | en       | 18           |
|    |                 | ragnargamingfr    | '99.181.91.52', '45.113.129.142' | fr       | 10           |
| 3  | 45.113.129.145  | trece_fn_         | '99.181.91.39', '45.113.129.145' | es       | 51           |
| 4  | 45.113.129.146  | beckslekitty      | '99.181.91.8', '45.113.129.146'  | en       | 18           |
| 5  | 45.113.129.148  | retired_viking    | '99.181.91.52', '45.113.129.148' | ar       | 91           |
|    |                 | flickflops        | '99.181.91.36', '45.113.129.148' | en       | 59           |
| 6  | 45.113.129.149  | khiela            | '99.181.91.36', '45.113.129.149' | fr       | 15           |
| 7  | 45.113.129.160  | xamzahh           | '99.181.91.28', '45.113.129.160' | en       | 92           |
| 8  | 45.113.129.167  | nutelada          | '99.181.91.19', '45.113.129.167' | es       | 34           |
|    |                 | im_rjn            | '99.181.91.14', '45.113.129.167' | pt       | 15           |
| 9  | 45.113.129.176  | naif_z4           | '99.181.91.52', '45.113.129.176' | ar       | 47           |
| 10 | 45.113.129.220  | un1corn_g1rl      | '99.181.91.14', '45.113.129.220' | en       | 20           |
|    |                 | kikologo          | '99.181.91.8', '45.113.129.220'  | es       | 19           |
|    |                 | foine             | '99.181.91.8', '45.113.129.220'  | fr       | 9            |
| 11 | 45.113.129.222  | juustik_          | '99.181.91.44', '45.113.129.222' | de       | 22           |
| 12 | 45.113.129.250  | dragonsniper43    | '99.181.91.16', '45.113.129.250' | en       | 10           |
| 13 | 45.113.130.238  | st00sh            | '99.181.91.27', '45.113.130.238' | en       | 435          |
| 14 | 45.113.130.242  | kymopt            | '99.181.91.8', '45.113.130.242'  | pt       | 268          |
|    |                 | angelanna01       | '99.181.91.16', '45.113.130.242' | en       | 9            |
| 15 | 45.113.130.245  | vgbootcamp        | '99.181.91.44', '45.113.130.245' | en       | 802          |
|    |                 | lapinoudantan     | '99.181.91.59', '45.113.130.245' | fr       | 68           |

After checking the IP location database, we see that `45.113.129.*` and `45.113.130.*` are Twitch's servers located in Hong Kong.

#### (2) Result, ignore outliers
The following figure is the result we get if we exclude the 16 server IPs mentioned in the previous section.

<img src="/images/channel-2.png" width="600">
