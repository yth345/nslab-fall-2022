import csv
import os

# day = ['2022-09-06', '2022-09-07', '2022-09-12', '2022-09-13', '2022-09-14', '2022-09-15', '2022-09-16']
# hour = ['%.2d' %i for i in range(24)]

file_list = os.listdir('./channel_new/')
channel_set = []
group_set = []
channel_cnt = []
for i in range(6):
    channel_set.append(set())
    group_set.append(set())
    channel_cnt.append([0, 0, 0])  # [channel cnt, total viewer cnt, max viewer cnt]

for filename in file_list:
    path = f'./channel_new/{filename}'
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            user_login = row[0]
            ip_list = row[1].strip('"').lstrip('{').rstrip('}').split(',')
            ip_list = [ip.strip().strip("'") for ip in ip_list]
            language = row[2]
            viewer_cnt = int(row[3])
            for ip in ip_list:
                if ip == 'set()':
                    continue
                if ip[:9] == '99.181.91':
                    idx = 0
                elif ip[:10] == '99.181.106' or ip[:10] == '99.181.107':
                    idx = 1
                elif ip[:10] == '45.113.129' or ip[:10] == '45.113.130':
                    idx = 2
                elif ip[:10] == '52.223.247':
                    idx = 3
                elif ip[:8] == '163.28.5':
                    idx = 4
                else:
                    idx = 5

                channel_set[idx].add(user_login)
                group_set[idx].add(ip)
                channel_cnt[idx][0] += 1
                channel_cnt[idx][1] += viewer_cnt
                if (viewer_cnt > channel_cnt[idx][2]):
                    channel_cnt[idx][2] = viewer_cnt

for i in range(6):
    if channel_cnt[i][0] == 0:
        continue
    print(f'g{i+1} unique ip cnt: {len(group_set[i])}; max viewer cnt: {channel_cnt[i][2]}; unique channel cnt: {len(channel_set[i])}')
