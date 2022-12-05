## 1125 Probes from Big 5 Countries
- Countries: US, UK, CA, FR, DE
- Probing time (UTC): 
  - US (Seattle): 2022-11-21 03:39 ~ 2022-11-22 02:55
  - UK (London): 2022-11-22 02:56 ~ 2022-11-23 02:39
  - CA (Vancouver): 2022-11-23 02:40 ~ 2022-11-24 01:15
  - FR (Paris): 2022-11-24 01:16 ~ 2022-11-25 00:15
  - DE (Berlin): 2022-11-25 00:16 ~ 2022-11-25 23:07

### 1. Data Processing
#### (1) Original files
__edgs/__
- Records the edge servers found by each channel in each probing round.
- filenames: the time the probing round started, e.g., `edgs/2022-11-23T02.42.57.770Z.tsv`
- columns: `timestamp`, `edge_hostname`, `channel_name(user_login)`

__strm/__
- Records the list of active channels (include their stream information) that the next probing round should probe.
- filenames: the time the collecting process started, always earlier than each probing round (filenames in __edgs/__), e.g., `strm/2022-11-23T02.40.36.315Z.json.txt`
- each line is a json object, recording the following attributes of streams: `id`, `user_id`, `user_login`, `user_name`, `game_id`, `game_name`, `type`, `title`,
`viewer_count`, `started_at`, `thumbnail_url`, `tag_ids`, `is_mature`

#### (2) Processed files
__edgs-w-info/__
- Mapped the stream information from __strm/__ to __edgs/__ using `user_login`.
Each probe was mapped from the __strm/__ files that has a closest time that is earlier than the probe.
- filenames: same as __edgs/__
- columns: `user_login`, `probe_t`, `hostname`, `language`, `viewer_cnt`

__edgs-hour/__
- Categorize each probe in __edgs-w-info/__ by the hour of the probe.
- filenames: the hour of the probes, e.g., `edgs-hour/2022-11-23T02.csv`
- columns: `user_login`, `probe_t`, `hostname`, `language`, `viewer_cnt`

__server/__  (US, UK, DE)
- Get the IP address of each hostname. Each row records an unique IP found from a country in an hour.
- filenames: same as __edgs-hour/__
- columns: `IP`, `hostname_list`, `unique_channel_cnt`, `language_list`, `max_viewer_cnt`


### 2. Discoveries
CA, 2022-11-23 H02
number of unique IPs: 1055

`video-edge-<6-bit code>.<3-bit IATA code><2-bit num>.abs.hls.ttvnw.net`   
`video-edge-<6-bit code>.<3-bit IATA code><2-bit num>.no-abs.hls.ttvnw.net`  
e.g., video-edge-c55b1c.arn03.abs.hls.ttvnw.net  

| IP range           | IATA code     | # of unique IPs |
| ------------------ | ------------- | --------------- |
| 52.223.192.*       | ams02         | 25  |
| 52.223.194.*       | lhr03, waw02, mad02, prg03 | 44 |
| 52.223.195.*       | cdg02         | 101 |
| 52.223.197.*       | mad01         | 66  |
| 52.223.199.*       | ber01, arn04, waw02 | 54 |
| 52.223.200.*       | fra05, osl01  | 51  |
| 52.223.201.*       | muc01, mad02  | 36  |
| 52.223.202.*       | cdg10, mad02, prg03 | 41 |
| 52.223.203.*       | lhr08, mil02, ber01 | 49 |
| 52.223.204.*       | hel03         | 34  |
| 52.223.205.*       | lhr08, vie02  | 32  |
| 52.223.217/218.*   | tyo03, tyo05  | 42  |
| 99.181.64/65.*     | fra05         | 75  |
| 99.181.66.*        | fra06, cph01  | 61  |
| 99.181.67.*        | ams03         | 30  |
| 99.181.68.*        | mil02, vie02  | 41  |
| 99.181.69.*        | mrs02, cdg10  | 41  |
| 99.181.88/89.*     | tyo03, tyo05  | 23  |
| 185.42.204/205.*   | arn03, fra02  | 161 |
| 185.42.206.*       | lhr03         | 24  |


`getaddrinfo EAI_AGAIN video-weaver.<3-bit IATA code><2-bit num>.hls.ttvnw.net`  
e.g., getaddrinfo EAI_AGAIN video-weaver.tyo03.hls.ttvnw.net

| IP                 | IATA code     |
| ------------------ | ------------- |
| 45.113.131.10      | tyo03         |
| 52.223.198.17      | mil02         |
| 99.181.79.2        | fra05         |
| 99.181.79.14       | fra02         |

