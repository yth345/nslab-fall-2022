import csv
import sys
from datetime import date, datetime

# 18 countries
country = ['Russian', 'Brazil', 'Ukraine', 'South_Korea', 'Spain', 'United_Kingdom', 
           'Canada', 'France', 'Netherlands', 'Germany', 'Japan', 'Australia', 
           'Denmark', 'Poland', 'Sweden', 'Italy', 'Turkey', 'United_States']
start_d = date(2021, 4, 1)
end_d = date(2021, 7, 31)

# for large datasets, uncomment the next line
csv.field_size_limit(sys.maxsize)

# process data
country_server = []
all_server_set = set()
for a_country in country:
    server_set = set()
    with open(f'./mongodb-data/{a_country}.csv') as file:
        reader = csv.reader(file)
        file.readline()
        for row in reader:
            probe_start = datetime.fromisoformat(row[3]).date()
            probe_end = datetime.fromisoformat(row[4]).date()
            if probe_start < start_d or probe_end > end_d:
                continue
            if row[5] == 'None':
                continue
            addr_pool = row[5].lstrip('[').rstrip(']').split(',')
            addr_pool = [e.strip().strip("'") for e in addr_pool]
            for ip in addr_pool:
                server_set.add(ip)
                all_server_set.add(ip)
    country_server.append(server_set)


# greedy algorithm
selected_country = []
print(f'inital server count: {len(all_server_set)}')
while len(all_server_set) > 0:
    max_cover_cnt = 0
    idx = 0
    for i in range(len(country_server)):
        cover_server_cnt = len(all_server_set.intersection(country_server[i]))
        if cover_server_cnt > max_cover_cnt:
            max_cover_cnt = cover_server_cnt
            idx = i

    selected_country.append(country[idx])
    all_server_set = all_server_set.difference(country_server[idx])
    for i in range(len(country_server)):
        country_server[i] = country_server[i].difference(country_server[idx])
    print(f'select {country[idx]}, undiscovered server count: {len(all_server_set)}')

print(f'selected countries:\n{selected_country}')
