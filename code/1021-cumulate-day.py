import csv
import os
from datetime import date

target_day = date(year=2022, month=9, day=12)

channel_dict = dict()
filename_lst = os.listdir('./channel_n/')
for filename in filename_lst:
    day = date.fromisoformat(filename[:10])
    if day != target_day:
        continue

    path = f'./channel_n/{filename}'
    with open(path, 'r') as rf:
        rf.readline()
        reader = csv.reader(rf)
        for row in reader:
            channel = row[0]
            server_set = row[1].strip('"').lstrip('{').rstrip('}').split(',')
            server_set = set([ip.strip().strip("'") for ip in server_set])
            language = row[2]
            viewer_cnt = int(row[3])

            if channel not in channel_dict:
                channel_dict[channel] = [server_set, [language], viewer_cnt]
            else:
                new_server_set = server_set.union(channel_dict[channel][0])
                old_viewer_cnt = channel_dict[channel][2]
                if old_viewer_cnt > viewer_cnt:
                    viewer_cnt = old_viewer_cnt
                prev_language = channel_dict[channel][1]
                if language not in prev_language:
                    prev_language.append(language)
                channel_dict[channel] = [new_server_set, prev_language, viewer_cnt]

write_path = f'./channel_day/{target_day.isoformat()}.csv'
with open(write_path, 'w', newline='') as wf:
    writer = csv.writer(wf)
    writer.writerow(['user_login', 'server_set', 'language', 'viewer_count'])
    for key, value in channel_dict.items():
        server_set = value[0]
        if 'set()' in server_set:
            server_set -= {'set()'}
        writer.writerow([key, value[0], value[1], value[2]])