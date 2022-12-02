## 1125 Probes from Big 5 Countries
- Countries: US, UK, CA, FR, DE
- Probing time (UTC): 
  - US: 2022-11-21 03:39 ~ 2022-11-22 02:55
  - UK: 2022-11-22 02:56 ~ 2022-11-23 02:39
  - CA: 2022-11-23 02:40 ~ 2022-11-24 01:15
  - FR: 2022-11-24 01:16 ~ 2022-11-25 00:15
  - DE: 2022-11-25 00:16 ~ 2022-11-25 23:07

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

__edgs-hour-sv/__  (WIP)
- Get the IP address of each hostname. Each row records an unique IP found from a country in an hour.
- filenames: same as __edgs-hour/__
- columns: `IP`, `hostname_list`, `language_list`, `max_viewer_cnt`


### 2. Discoveries

