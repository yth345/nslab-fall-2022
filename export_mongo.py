from pymongo import MongoClient
import csv


client = MongoClient('localhost:25555')
db = client.Twitch
serverStatusResult = db.command('serverStatus')


# collections in DB
country = ['Taiwan', 'Russian', 'Brazil', 'Ukraine', 'South_Korea', 'SouthKorea', 'Spain', 
           'United_Kingdom', 'Canada', 'France', 'Netherlands', 'Germany', 'Japan', 'Australia', 
           'Denmark', 'Poland', 'Sweden', 'Italy', 'Turkey', 'United_States']

# export to same format
# columns: 'country', 'channel', 'language', 'start', 'end', 'addrPool', 'vpnServerId', 'viewerList', 'transactionList'
for a_country in country:
    filename = f'./mongodb-data/{a_country}.csv'
    print(f'start {a_country}...')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['country', 'channel', 'language', 'start', 'end', 'addrPool', 'vpnServerId', 'viewerList', 'transactionList'])

        for a_doc in db[a_country].find():
            new_row = [a_country, a_doc['channel'], a_doc['language'], a_doc['start'], a_doc['end']]
            # addrPool column
            if 'serverPool' in a_doc:
                new_row.append(a_doc['serverPool'])
            elif 'addrPool' in a_doc:
                new_row.append(a_doc['addrPool'])
            else:
                new_row.append('None')
            # vpnServerId column
            if 'vpnServerId' in a_doc:
                new_row.append(a_doc['vpnServerId'])
            else:
                new_row.append('None')
            # viewerCnt column
            if 'viewerList' in a_doc:
                new_row.append(a_doc['viewerList'])
            else:
                new_row.append('None')
            # transactionList column
            new_row.append(a_doc['transactionList'])

            writer.writerow(new_row)
    print('done')


# combine two South Korea datasets, write to South_Korea.csv
with open('./mongodb-data/South_Korea.csv', 'a', newline='') as wf:
    writer = csv.writer(wf)
    with open('./mongodb-data/SouthKorea.csv', 'r', newline='') as rf:
        reader = csv.reader(rf)
        rf.readline()
        for a_row in reader:
            writer.writerow(a_row)
