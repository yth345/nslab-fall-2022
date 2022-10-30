# process the new full dataset crawled from nslab
# run this code under CIG/

import os
import csv
from datetime import datetime

cnt = 0
folder_list = os.listdir('./tsvs/')

for folder_name in folder_list:
    with open(f'./temporal/{folder_name}.csv', 'w', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(['minute', 'server_set'])

        minute_set = [set() for i in range(60)]

        rd_path = f'./tsvs/{folder_name}/'
        for filename in os.listdir(rd_path):
            fpath = rd_path + filename
            with open(fpath, 'r') as rf:
                reader = csv.reader(rf, delimiter='\t')
                for row in reader:
                    # ignore errors, such as
                    # 'Request failed with status code 403'
                    # 'socket hang up'
                    # ""Cannot read properties of null (reading 'value')""
                    if '.' not in row[1]:
                        continue

                    minute = int(row[0][14:16])
                    minute_set[minute].add(row[1])

        # write 60 rows of minute data to wf
        dt = datetime.fromisoformat(folder_name)
        for i in range(60):
            new_dt = datetime(dt.year, dt.month, dt.day, dt.hour, i)
            if len(minute_set[i]) == 0:
                continue
            writer.writerow([new_dt, minute_set[i]])

    cnt += 1
    if cnt == 20:
        print('20 done')
        cnt = 0