import csv
import os

# day = ['2022-09-06', '2022-09-07', '2022-09-11', '2022-09-12', '2022-09-13', '2022-09-14', '2022-09-15', '2022-09-16']
day = ['2022-09-06']
hour = ['%.2d' %i for i in range(15, 24)]

# test how much percent of channels we need if we select from highest viewer cnt
for d in day:
    for h in hour:
        universe = set()
        probes = []
        cnt = 0
        path = f'./channel_new/{d}T{h}.csv'
        with open(path, 'r') as f:
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                ip_list = row[1].strip('"').lstrip('{').rstrip('}').split(',')
                ip_list = [ip.strip().strip("'") for ip in ip_list]
                # language = row[2].strip('"').lstrip('[').rstrip(']').split(',')
                # language = [lan.strip().strip("'") for lan in language]
                viewer_cnt = int(row[3])
                if ip_list == ['set()']:
                    continue
                for ip in ip_list:
                    ### change this line for different clusters of servers ###
                    if ip[:10] == '52.223.247':
                        universe.add(ip)
                probes.append([set(ip_list), viewer_cnt])
                cnt += 1

        probes.sort(key=lambda x: x[1], reverse=True)  

        for i in range(len(probes)):
            universe = universe.difference(probes[i][0])
            if len(universe) == 0:
                print(f'{d}T{h} select cnt: {i + 1}, total probe cnt: {cnt}, percentage: {(i + 1) / cnt}')
                break

