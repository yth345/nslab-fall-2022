import json
import csv
import os
from datetime import datetime, timedelta

# raws missing: 2022-09-07T08, 2022-09-16T07
raw_list = os.listdir('./raws/')

# ignore subdirectories in raws, create a big dictionary for all channels
info_dict = dict()
for filename in raw_list:
    path = './raws/' + filename
    with open(path, 'r') as rf:
        reader = csv.reader(rf, delimiter='\t')
        for row in reader:
            dt = datetime.fromisoformat(row[0][:13])
            hour_dt = datetime(dt.year, dt.month, dt.day, dt.hour)
            raw = json.loads(row[1])
            for data in raw['data']:
                user_login = data['user_login']
                language = data['language']
                viewer_cnt = data['viewer_count']

                if (user_login, hour_dt) in info_dict:
                    # keep the largest viewer count in an hour
                    prev_viewer_cnt = info_dict[(user_login, hour_dt)][1]
                    if viewer_cnt > prev_viewer_cnt:
                        info_dict[(user_login, hour_dt)] = [language, viewer_cnt]
                else:
                    info_dict[(user_login, hour_dt)] = [language, viewer_cnt]

print(len(info_dict))  # total 5241625 

cnt = 0
# map info to channel using user_login
channel_list = os.listdir('./channel/')
for filename in channel_list[:3]:
    read_path = './channel/' + filename
    write_path = './channel_n/' + filename

    with open(read_path, 'r') as rf:
        reader = csv.reader(rf)
        rf.readline()
        with open(write_path, 'w', newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow(['user_login', 'server_set', 'language', 'viewer_count'])

            for row in reader:
                user_login = row[0]
                ip_set = row[1]
                hour_dt = datetime.fromisoformat(filename[:13])
                find_match = False

                while not find_match:
                    if (user_login, hour_dt) in info_dict:
                        language = info_dict[(user_login, hour_dt)][0]
                        viewer_cnt = info_dict[(user_login, hour_dt)][1]
                        find_match = True
                    else:
                        hour_dt = hour_dt - timedelta(hours=1)
                        if hour_dt < datetime(year=2022, month=9, day=1):
                            print(f'{(user_login, hour_dt)} no info')
                            break
                
                writer.writerow([user_login, ip_set, language, viewer_cnt])

    cnt += 1
    if cnt == 20:
        print('20 done')
        cnt = 0