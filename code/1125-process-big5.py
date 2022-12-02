import csv
import os
import json
from datetime import datetime

# country = ['CA', 'DE', 'FR', 'UK', 'US']
# country = ['CA']
country = ['DE', 'FR', 'UK', 'US']

# to do
# map stream info to probes,
# categorize the probes with hour


def process_data(c):
    probe_file_list = sorted(os.listdir(f'./{c}/edgs/'))
    stream_info_file_list = sorted(os.listdir(f'./{c}/strm/'))

    info_dict = dict()
    for fn in stream_info_file_list:
        info_t = datetime.fromisoformat(fn[:-14].replace('.', ':'))
        path = f'./{c}/strm/{fn}'
        with open(path, 'r') as f:
            for row in f:
                raw = json.loads(row)
                for data in raw['data']:
                    user_login = data['user_login']
                    language = data['language']
                    viewer_cnt = int(data['viewer_count'])

                    if user_login not in info_dict:
                        info_dict[user_login] = [[info_t, language, viewer_cnt]]
                    else:
                        info_dict[user_login].append([info_t, language, viewer_cnt])

    ttl_probe_cnt = 0
    for fn in probe_file_list:
        probe_t = datetime.fromisoformat(fn[:-9].replace('.', ':'))
        r_path = f'./{c}/edgs/{fn}'
        with open(r_path, 'r') as rf:
            reader = csv.reader(rf, delimiter='\t')
            w_path = f'./{c}/edgs-w-info/{fn[:-4]}.csv'
            with open(w_path, 'w', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerow(['user_login', 'probe_t', 'hostname', 'language', 'viewer_cnt'])
                for row in reader:
                    # compare time and find the closest info before probe
                    ttl_probe_cnt += 1
                    ptime = row[0]
                    hostname = row[1]
                    user_login = row[2]
                    entry_cnt = len(info_dict[user_login])
                    if entry_cnt == 1:
                        language = info_dict[user_login][0][1]
                        viewer_cnt = info_dict[user_login][0][2]

                    for i in range(entry_cnt - 1):
                        curr_info = info_dict[user_login][i]
                        next_info = info_dict[user_login][i + 1]
                        next_t = next_info[0]
                        if probe_t > next_t:
                            # last entry
                            if (i + 1) == (entry_cnt - 1):
                                language = next_info[1]
                                viewer_cnt = next_info[2]
                            continue
                        else:
                            language = curr_info[1]
                            viewer_cnt = curr_info[2]
                            break
                    writer.writerow([user_login, ptime, hostname, language, viewer_cnt])
        print(f'{c}, {fn[:-4]} done')
    print(f'total probe cnt: {ttl_probe_cnt}')

    
def write_to_hour(c):
    write_cnt = 0
    for fn in sorted(os.listdir(f'./{c}/edgs-w-info/')):
        r_path = f'./{c}/edgs-w-info/{fn}'
        hour_dict = dict()
        with open(r_path, 'r') as f:
            f.readline()
            reader = csv.reader(f)
            for row in reader:
                curr_dt = datetime.fromisoformat(row[1][:-1])
                h = '%.2d' %curr_dt.hour
                curr_hour = f'{curr_dt.date()}T{h}'
                if curr_hour not in hour_dict:
                    hour_dict[curr_hour] = [row]
                else:
                    hour_dict[curr_hour].append(row)

        # remember to clear files in edgs-hour before running this
        hour_file_list = os.listdir(f'./{c}/edgs-hour/')
        for key, value in hour_dict.items():
            w_fn = f'{key}.csv'
            w_path = f'./{c}/edgs-hour/{w_fn}'
            if w_fn in hour_file_list:
                with open(w_path, 'a', newline='') as f:
                    writer = csv.writer(f)
                    for row in value:
                        write_cnt += 1
                        writer.writerow(row)
            else:
                with open(w_path, 'w', newline='') as f:
                    writer = csv.writer(f)
                    for row in value:
                        write_cnt += 1
                        writer.writerow(row)
        # print(f'{c}, {fn[:-4]} hour done')
    print(f'write row cnt: {write_cnt}')


    '''
    # problem:
    # is it possible that probes in a later filename has records earlier than prev filenames?
    # solution:
    # open each edgs-w-info file, keep a dictionary of hours we have,
    # after reading all lines, write to each hour file (if exist filename use 'a', otherwise use 'w')

    first_probe = True
    hour_probe = []
    target_hour = '00'
    for fn in sorted(os.listdir(f'./{c}/edgs-w-info/')):
        r_path = f'./{c}/edgs-w-info/{fn}'
        with open(r_path, 'r') as rf:
            rf.readline()
            reader = csv.reader(rf)
            for row in reader: 
                curr_dt = datetime.fromisoformat(row[1][:-1])
                if first_probe:
                    target_hour = '%.2d' %curr_dt.hour
                    hour_probe.append(row)
                    first_probe = False
                    continue
                curr_hour = '%.2d' %curr_dt.hour
                if curr_hour == target_hour:
                    hour_probe.append(row)
                else:
                    w_path = f'./{c}/edgs-hour/{curr_dt.date()}T{target_hour}.csv'
                    with open(w_path, 'w', newline='') as wf:
                        writer = csv.writer(wf)
                        writer.writerow(['user_login', 'probe_t', 'hostname', 'language', 'viewer_cnt'])
                        for p in hour_probe:
                            writer.writerow(p)
                    print(f'{target_hour} done')
                    target_hour = curr_hour
                    hour_probe = [row]

    # write last hour
    w_path = f'./{c}/edgs-hour/{hour_probe[0][1][:13]}.csv'
    with open(w_path, 'w', newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow(['user_login', 'probe_t', 'hostname', 'language', 'viewer_cnt'])
        for p in hour_probe:
            writer.writerow(p)
    '''


for c in country:
    process_data(c)
    write_to_hour(c)
    # process_data(f'big-5/{c}')
    # write_to_hour(f'big-5/{c}')

    print(f'{c} done')
    ttl_row_cnt = 0
    for fn in sorted(os.listdir(f'./{c}/edgs-hour/')):
        r_path = f'./{c}/edgs-hour/{fn}'
        with open(r_path, 'r') as f:
            reader = csv.reader(f)
            row_count = sum(1 for row in reader)
            ttl_row_cnt += row_count
            print(f'{c} {fn[:-4]} row cnt: {row_count}')
    print(ttl_row_cnt)

