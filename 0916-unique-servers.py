import csv
import sys
from datetime import datetime, date
import matplotlib.pyplot as plt

# 1. data format (each row)
# country, channel, language, start, end, addrPool, vpnServerId, viewerList, transactionList
# 2. transactionList format
# {'YYYY-mm-ddTHH:MM:SS': '<ip1>', 'YYYY-mm-ddTHH:MM:SS': '<ip2>'}

country = 'Taiwan'

# for large datasets, uncomment the next line
# csv.field_size_limit(sys.maxsize)

server_cnt_dict = dict()
with open(f'./mongodb-data/{country}.csv') as file:
    reader = csv.reader(file)
    file.readline()
    for row in reader:
        transaction_list = row[-1].lstrip('{').rstrip('}').split(',')

        for trans in transaction_list:
            entry = trans.rsplit(':', 1)
            dt = datetime.fromisoformat(entry[0].strip(' ').strip("'"))
            ip = entry[1].strip(' ').strip("'")

            d = date(dt.year, dt.month, dt.day)
            if d in server_cnt_dict:
                ip_exist = False
                for i, val in enumerate(server_cnt_dict[d]):
                    if val[0] == ip:
                        server_cnt_dict[d][i] = (ip, val[1] + 1)
                        ip_exist = True
                        break
                if not ip_exist:
                    server_cnt_dict[d].append((ip, 1))
            else:
                server_cnt_dict[d] = [(ip, 1)]
    


# draw daily number of unique servers
crawl_dates = []
unique_server_cnt = []
probe_cnt = []
for k in server_cnt_dict.keys():
    crawl_dates.append(k)
    unique_server_cnt.append(len(server_cnt_dict[k]))
    p_cnt = 0
    for val in server_cnt_dict[k]:
        p_cnt += val[1]
    probe_cnt.append(p_cnt)


fig, ax = plt.subplots(1, 1, figsize=(8,6))
ax.set_axisbelow(True)
ax.bar(crawl_dates, unique_server_cnt)
ax.grid()

plt.xlim(datetime(2020, 10, 1), datetime(2021, 5, 1))

plt.xticks(rotation=20)
plt.title(f'Number of Unique Servers Each Day ({country})')
plt.xlabel('Date')
plt.ylabel('Number of unique servers')

plt.subplots_adjust(bottom=0.15)
plt.savefig(f'./images/daily-servers/{country}.png', dpi=300)