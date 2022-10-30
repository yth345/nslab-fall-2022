# process the new full dataset crawled from nslab
# run this code under CIG/

import os
import csv

cnt = 0
folder_list = os.listdir('./tsvs/')

for folder_name in folder_list:
    with open(f'./channel/{folder_name}.csv', 'w', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(['user_login', 'server_set'])

        rd_path = f'./tsvs/{folder_name}/'
        for filename in os.listdir(rd_path):
            fpath = rd_path + filename
            ip_set = set()
            with open(fpath, 'r') as rf:
                reader = csv.reader(rf, delimiter='\t')
                for row in reader:
                    # ignore errors, such as
                    # 'Request failed with status code 403'
                    # 'socket hang up'
                    # ""Cannot read properties of null (reading 'value')""
                    if '.' not in row[1]:
                        continue
                    ip_set.add(row[1])

            # get channel name
            channel_name = filename[13:-4]
            writer.writerow([channel_name, ip_set])

    cnt += 1
    if cnt == 20:
        print('20 done')
        cnt = 0
