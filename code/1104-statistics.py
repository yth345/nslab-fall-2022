import csv

day = '2022-09-12'
hour = ['%.2d' %i for i in range(24)]
# hour = ['00']

# 1. avg number of IPs for a language
# 2. avg viewer cnt?

lan_dict = dict()
for h in hour:
    path = f'./channel_new/{day}T{h}.csv'
    with open(path, 'r') as f:
        f.readline()
        reader = csv.reader(f)
        for row in reader:
            ip_cnt = len(row[1].strip('"').lstrip('{').rstrip('}').split(','))
            language = row[2].lstrip('[').rstrip(']')
            viewer_cnt = int(row[3])
            if language not in lan_dict:
                lan_dict[language] = [ip_cnt]
            else:
                lan_dict[language].append(ip_cnt)

result = []
for key, item in lan_dict.items():
    result.append([key, len(item), max(item), sum(item) / len(item)])
result.sort(key=lambda x: (x[2], x[3]), reverse=True)

w_path = f'./channel_hour/{day}-stat.csv'
with open(w_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['language', 'channel cnt', 'max IP', 'avg IP cnt'])
    for r in result:
        writer.writerow(r)



