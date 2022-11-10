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
The entries we find relevant to our purpose are: viewer_count, langauge

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
(1) **Greedy:** Select the channel that can cover the most uncovered server IPs, repeat until we reach set cover.  
(2) **Heuristic:** Select the channel with the most viewer count each round, repeat until we reach set cover.  

#### (1) Result
We can see that greedy and heuristic algorithm both performs well on reducing the number of channels that we need to probe, except for heuristic algorithm on hour 16 and hour 19.  
<img src="/images/channel-1.png" width="600">

If we take a look at what happend in the two hours, we found that some servers appear only in channels that have a few viewers.  
Summary:  
| Time          |
| ------------- |
| 2022-09-12T16 |
| 2022-09-12T19 |
