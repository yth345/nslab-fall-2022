import csv
import sys
from datetime import date, datetime
from itertools import combinations

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


# brute force find min set cover
country_idx = [i for i in range(len(country))]
for i in range(10, 19):  # to save time, try combinations from C(18, 10) to C(18, 18)
    found = 0
    for cb in combinations(country_idx, i):
        universe = all_server_set.copy()
        for c_idx in cb:
            universe = universe.difference(country_server[c_idx])
        if len(universe) == 0:
            print(f'C(18, {i}) found, combination: {[country[c] for c in cb]}')
            found = 1
    if found:
        break
    else:
        print(f'C(18, {i}) set cover not found')