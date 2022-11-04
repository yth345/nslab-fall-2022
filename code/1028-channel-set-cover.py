import csv
from itertools import combinations

day = '2022-09-12'
path = './channel_day/' + day + '-g2.csv'

all_channel_set = set()
ip_set_list = []
max_cardinality = 0
with open(path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        ip_set = row[1].strip('"').lstrip('{').rstrip('}').split(',')
        ip_set = set([ip.strip().strip("'") for ip in ip_set])
        if len(ip_set) > max_cardinality:
            max_cardinality = len(ip_set)
        ip_set_list.append(ip_set)
        all_channel_set = all_channel_set.union(ip_set)
channel_idx = [i for i in range(len(ip_set_list))]
print(f'num of IPs in {day}: {len(all_channel_set)}')

max_card_list = []
cnt = 0
for i in range(len(ip_set_list) - 1, 0, -1):
    if len(ip_set_list[i]) == max_cardinality:
        max_card_list.append(ip_set_list[i])
        cnt += 1
    else:
        break

# get the approximate number of channels needed to cover all IPs
# greedy choose the set with the max cardinality
# ip_set_list is sorted in ascending order of set cardinality

# try select in the first round different max cardinality sets
for i in range(len(max_card_list)):
    chosen_set = []
    universe = all_channel_set.copy()
    ip_set_list_cp = ip_set_list.copy()
    print(f'{i+1}.\nuncoverd IP cnt: {len(universe)}', end='')
    
    selected = max_card_list[i]
    chosen_set.append(selected)
    universe = universe.difference(selected)
    print(f' {len(universe)}', end='')
    ip_set_list_cp.remove(selected)
    for j in range(len(ip_set_list_cp)):
        ip_set_list_cp[j] = ip_set_list_cp[j].difference(selected)
    ip_set_list_cp.sort(key=len)
    
    idx = len(ip_set_list_cp) - 1
    while (len(universe) > 0):
        selected = ip_set_list_cp[idx]
        chosen_set.append(selected)
        universe = universe.difference(selected)
        print(f' {len(universe)}', end='')
        for j in range(idx - 1, 0, -1):
            ip_set_list_cp[j] = ip_set_list_cp[j].difference(selected)
        ip_set_list_cp.pop()
        ip_set_list_cp.sort(key=len)
        idx -= 1
    print(f'\napproximate solution {i+1}: {len(chosen_set)} channels')

# get optimal solution
# let F be the set of all server IP sets, S be a server IP set
# the approximate ratio for greedy is H(max{|S|: S in F}), which is H(20) = 2.3 at 2022-09-12
# we found 22 channels by greedy approximate, so the optimal solution should be 10~22
# C(481, 10) = 1.66E20, C(481, 22) = 5.55E37, not feasible

