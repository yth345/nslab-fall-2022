import csv
import os

##### options #####
# group: 2, 3
###################
def cover_hour(group):
    if group == 2:
        dates = g2_dates
        prefix = ip_prefix_g2
    elif group == 3:
        dates = g3_dates
        prefix = ip_prefix_g3
    else:
        print('please enter a valid group: 2 or 3')
        return

    # get the set of IPs in a server cluster
    all_ip_set = set()
    ip_list = []
    for h in hour:
        ip_hour = set()
        for d in dates:
            if f'{d}T{h}' not in filename:
                continue
            path = f'./channel_server/{d}T{h}-server.csv'
            with open(path, 'r') as f:
                f.readline()
                reader = csv.reader(f)
                for row in reader:
                    ip = row[0]
                    if ip[:10] in prefix:
                        ip_hour.add(ip)
        if len(ip_hour) != 0:
            ip_list.append([h, ip_hour])
            all_ip_set = all_ip_set.union(ip_hour)
    for i in range(len(ip_list)):
        print('hour:', ip_list[i][0], '; ip_cnt:', len(ip_list[i][1]))

    # find the minimum set of hours that can cover all server IPs
    ip_list.sort(key=lambda x: len(x[1]))
    chosen_hour = []
    idx = len(ip_list) - 1
    while(len(all_ip_set) > 0):
        selected_ips = ip_list[idx][1]
        all_ip_set = all_ip_set.difference(selected_ips)
        chosen_hour.append(f'{ip_list[idx][0]}')
        for i in range(idx - 1, 0, -1):
            ip_list[i][1] = ip_list[i][1].difference(selected_ips)
        ip_list.pop()
        ip_list.sort(key=lambda x: len(x[1]))
        idx -= 1

    print('select hour:', chosen_hour)
    return

hour = ['%.2d' %i for i in range(24)]

ip_prefix_g2 = ['99.181.106', '99.181.107']
g2_dates = ['2022-09-11', '2022-09-12', '2022-09-13', '2022-09-14', '2022-09-15']

ip_prefix_g3 = ['45.113.129', '45.113.130']
g3_dates = ['2022-09-06', '2022-09-11', '2022-09-12', '2022-09-13', '2022-09-15']

file_list = os.listdir('./channel_server/')
filename = [fn[:13] for fn in file_list]

# pass in 2 or 3
cover_hour(3)
