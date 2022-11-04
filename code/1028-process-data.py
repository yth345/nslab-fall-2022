import csv
import sys

# pick a whole day to test, 2022-09-12
day = ['2022-09-06', '2022-09-07', '2022-09-11', '2022-09-12', '2022-09-13', '2022-09-14', '2022-09-15', '2022-09-16']

# process 1 (280k -> 8k)
# re-group channels with same server ips 
# keep a record of which channel belongs to which group -> frozen set as key

for d in day:
    path = './channel_day/' + d + '.csv'
    channel_cnt = 0
    ip_group = dict()
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)

        for row in reader:
            channel_cnt += 1
            channel = row[0]
            ip_set = row[1].strip('"').lstrip('{').rstrip('}').split(',')
            ip_set = frozenset([ip.strip().strip("'") for ip in ip_set])
            if ip_set not in ip_group:
                ip_group[ip_set] = [channel]
            else:
                ip_group[ip_set].append(channel)
            
    print(d, channel_cnt, len(ip_group))

    w_path = './channel_day/' + d + '-g1.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in ip_group.items():
            writer.writerow([key, value])


# process 2 (8k -> 0.5k)
# if a set of IPs is subset of another set, keep only the larger set
# append the smaller set channels to bigger set channels

csv.field_size_limit(sys.maxsize) # the field that records channel list exceeds 131072

ip_set_list = []
single_ip_cnt = 0
multi_ip_cnt = 0
for d in day:
    path = './channel_day/' + d + '-g1.csv'
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            # format of first column: 
            # single ip: frozenset({'99.181.91.30'})
            # multiple ips: "frozenset({'99.181.91.51', '99.181.91.42', '99.181.91.36'})"
            ip_set = row[0].strip('"')[11:-2]
            ip_set = ip_set.split(',')
            ip_set = set([ip.strip().strip("'") for ip in ip_set])
            if ip_set == {'set()'}:
                continue
            ip_set_list.append(ip_set)
            if len(ip_set) == 1:
                single_ip_cnt += 1
            else:
                multi_ip_cnt += 1
    print(f'{d}, single ip cnt: {single_ip_cnt}, multi ip cnt: {multi_ip_cnt}')

    index, sorted_ip_set = zip(*sorted(enumerate(ip_set_list), key=lambda x: len(x[1])))

    subset_idx_map = []
    for i in range(len(sorted_ip_set)):
        for j in range(len(sorted_ip_set)-1, i, -1):
            if sorted_ip_set[i].issubset(sorted_ip_set[j]):
                subset_idx_map.append((index[i], index[j]))
                break
    print('reduce cnt:', len(subset_idx_map), 'remain cnt:', len(sorted_ip_set)-len(subset_idx_map))
    w_path = './channel_day/' + d + '-map.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['subset idx', 'joined group idx'])
        for i in range(len(subset_idx_map)):
            writer.writerow([subset_idx_map[i][0], subset_idx_map[i][1]])

    w_path = './channel_day/' + d + '-g2.csv'
    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        row_cnt = 0
        for i in range(len(sorted_ip_set)):
            removed = False
            for j in range(len(subset_idx_map)):
                if index[i] == subset_idx_map[j][0]:
                    removed = True
                    break
            if not removed:
                row_cnt += 1
                writer.writerow([row_cnt, sorted_ip_set[i]])

