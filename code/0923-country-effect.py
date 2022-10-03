import csv
import sys
from datetime import datetime, date, timedelta
import numpy as np

# phase 1: 2021-06-03 ~ 2021-06-14
country = ['Brazil', 'Canada', 'Denmark', 'Germany', 'Italy', 'Japan', 'Poland', 'Spain', 'Sweden', 'Turkey', 'Russian']
start_d = date(2021, 6, 3)
end_d = date(2021, 6, 14)

# for large datasets, uncomment the next line
csv.field_size_limit(sys.maxsize)

all_server_dict = dict()
country_server_list = []
for a_country in country:
    c_server_dict = dict()
    with open(f'./mongodb-data/{a_country}.csv') as file:
        reader = csv.reader(file)
        file.readline()
        for row in reader:
            transaction_list = row[-1].lstrip('{').rstrip('}').split(',')

            for trans in transaction_list:
                entry = trans.rsplit(':', 1)
                dt = datetime.fromisoformat(entry[0].strip(' ').strip("'"))
                ip = entry[1].strip(' ').strip("'")

                d = date(dt.year, dt.month, dt.day)
                if d < start_d or d > end_d:
                    continue

                if d in all_server_dict:
                    all_server_dict[d].add(ip)
                else:
                    all_server_dict[d] = {ip}
                if d in c_server_dict:
                    c_server_dict[d].add(ip)
                else:
                    c_server_dict[d] = {ip}

    country_server_list.append(c_server_dict)


crawl_dates = []
add_d = start_d
while add_d <= end_d:
    crawl_dates.append(add_d)
    add_d = add_d + timedelta(days=1)

all_unique_server_cnt = []
for d in crawl_dates:
    all_unique_server_cnt.append(len(all_server_dict[d]))


# 1.
# extract a country at a time and see how many unique servers are left
rm_c_server_cnt = []
for i in range(len(country)):
    s_cnt = []
    for d in crawl_dates:
        server_set = set()
        for j in range(len(country)):
            if i == j:
                continue
            if d in country_server_list[j]:
                server_set = server_set.union(country_server_list[j][d])
        s_cnt.append(len(server_set))
    rm_c_server_cnt.append(s_cnt)

with open('compare_country.npy', 'wb') as f:
    np.save(f, np.array(all_unique_server_cnt))
    for i in range(len(country)):
        np.save(f, np.array(rm_c_server_cnt[i]))

'''
# 2.
# try different combinations
# g1: Brazil, Canada, Japan
# g2: Brazil, Canada, Japan, Poland
# g3: Brazil, Canada, Japan, Poland, Turkey
# g4: Brazil, Canada, Japan, Poland, Germany
# g5: Brazil, Canada, Japan, Poland, Spain
# g6: Brazil, Canada, Japan, Poland, Turkey, Germany, Spain
g1 = []
g2 = []
g3 = []
g4 = []
g5 = []
g6 = []
for d in crawl_dates:
    s_set = set()
    s_set = s_set.union(country_server_list[0][d])
    s_set = s_set.union(country_server_list[1][d])
    s_set = s_set.union(country_server_list[5][d])
    g1.append(len(s_set))
    s_set = s_set.union(country_server_list[6][d])
    g2.append(len(s_set))

    s3_set = s_set.union(country_server_list[9][d])
    g3.append(len(s3_set))
    s4_set = s_set.union(country_server_list[3][d])
    g4.append(len(s4_set))
    s5_set = s_set.union(country_server_list[7][d])
    g5.append(len(s5_set))

    s6_set = s3_set.union(country_server_list[3][d])
    s6_set = s6_set.union(country_server_list[7][d])
    g6.append(len(s6_set))

with open('g1.npy', 'wb') as f:
    np.save(f, np.array(all_unique_server_cnt))
    np.save(f, np.array(g1))
    np.save(f, np.array(g2))
    np.save(f, np.array(g3))
    np.save(f, np.array(g4))
    np.save(f, np.array(g5))
    np.save(f, np.array(g6))
'''

