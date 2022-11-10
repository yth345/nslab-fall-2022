import csv
import copy

# --- algorithm option --- #
# 'greedy': select the set that can cover the most uncovered IPs
# 'h1': select from the most viewer count

def write_set_cover(day, h, alg='greedy'):
    path = f'./channel_new/{day}T{h}.csv'
    probes = []
    cnt = 0
    all_ip_set = set()
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            cnt += 1
            ip_set = row[1].strip('"').lstrip('{').rstrip('}').split(',')
            ip_set = set([ip.strip().strip("'") for ip in ip_set])
            if ip_set == {'set()'}:
                cnt -= 1
                continue
            all_ip_set = all_ip_set.union(ip_set)
            language = row[2]
            viewer_count = int(row[3])
            probes.append([cnt, ip_set, language, viewer_count])
    print(f'{day}T{h} channel cnt: {cnt}, num of unique servers: {len(all_ip_set)}')

    probes_cp = copy.deepcopy(probes)
    universe = all_ip_set.copy()
    result = []

    if (alg == 'greedy'):
        probes.sort(key=lambda x: len(x[1]))  # sort by ip set cardinality, ascending order
        while (len(universe) > 0):
            selected = probes.pop()
            result.append(probes_cp[selected[0] - 1])
            universe = universe.difference(selected[1])
            for i in range(len(probes)):
                probes[i][1] = probes[i][1].difference(selected[1])
            probes.sort(key=lambda x: len(x[1]))
        w_path = f'./channel_hour/{day}T{h}.csv'

    elif (alg == 'h1'):
        probes.sort(key=lambda x: x[3])
        while (len(universe) > 0):
            selected = probes.pop()
            result.append(probes_cp[selected[0] - 1])
            universe = universe.difference(selected[1])
        w_path = f'./channel_hour/{day}T{h}_h1.csv'

    print(f'{alg} solution: {len(result)} channels')

    with open(w_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(result)):
            writer.writerow(result[i])


day = '2022-09-12'
hour = ['%.2d' %i for i in range(24)]
for h in hour:
    write_set_cover(day, h, 'h1')

