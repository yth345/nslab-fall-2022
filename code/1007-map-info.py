import json
import csv
import os

# raws missing: 2022-09-07T08, 2022-09-16T07
raw_list = os.listdir('./raws/')
# raw_list = ['2022-09-13T06raw.json.tsv']

# ignore subdirectories in raws, create a big dictionary for all channels
info_dict = dict()
for filename in raw_list:
    path = './raws/' + filename
    with open(path, 'r') as rf:
        reader = csv.reader(rf, delimiter='\t')
        for row in reader:
            raw = json.loads(row[1])
            for data in raw['data']:
                user_login = data['user_login']
                language = data['language']
                viewer_cnt = int(data['viewer_count'])

                if user_login in info_dict:
                    # keep the largest viewer count
                    prev_viewer_cnt = info_dict[user_login][1]
                    if viewer_cnt > prev_viewer_cnt:
                        info_dict[user_login][1] = viewer_cnt
                    if language not in info_dict[user_login][0]:
                        info_dict[user_login][0].append(language)
                else:
                    info_dict[user_login] = [[language], viewer_cnt]

# print(len(info_dict))  # total 748335 channels

cnt = 0
# map info to channel using user_login
channel_list = os.listdir('./channel/')
for filename in channel_list:
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
                if user_login in info_dict:
                    language = info_dict[user_login][0]
                    viewer_cnt = info_dict[user_login][1]
                else:
                    print(f'{user_login} no info')
                    language = 'NaN'
                    viewer_cnt = 0
                
                writer.writerow([user_login, ip_set, language, viewer_cnt])

    cnt += 1
    if cnt == 20:
        print('20 done')
        cnt = 0

