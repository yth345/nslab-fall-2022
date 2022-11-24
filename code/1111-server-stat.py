import csv
import os

file_list = os.listdir('./channel_new/')

for filename in file_list:
    path = f'./channel_new/{filename}'
    server_dict = dict()
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            ip_list = row[1].strip('"').lstrip('{').rstrip('}').split(',')
            ip_list = [ip.strip().strip("'") for ip in ip_list]
            lan_set = row[2].strip('"').lstrip('[').rstrip(']').split(',')
            lan_set = set([lan.strip().strip("'") for lan in lan_set])
            viewer_cnt = int(row[3])
            for ip in ip_list:
                if ip == 'set()':
                    continue
                if ip not in server_dict:
                    server_dict[ip] = [1, lan_set, viewer_cnt]
                else:
                    channel_cnt = server_dict[ip][0] + 1
                    langauge = server_dict[ip][1].union(lan_set)
                    cumu_viewer = server_dict[ip][2] + viewer_cnt
                    server_dict[ip] = [channel_cnt, langauge, cumu_viewer]

    print(f'{filename} unique server cnt: {len(server_dict)}')
    server_list = []
    for key, value in server_dict.items():
        server_list.append([key, value[0], value[1], value[2]])
    server_list.sort(key=lambda x: x[0])

    w_path = f'./channel_server/{filename}-server.csv' 
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['server_ip', 'channel_cnt', 'language', 'cumu_viewer_cnt'])
        for s in server_list:
            writer.writerow(s)

