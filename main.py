import sys
import requests
import json
from datetime import datetime as dt

time_format='%Y-%m-%dT%H:%M:%S.%fZ'
databaseName='databaseName'
creation='createdAt'
snapshots_path = None
server= None

def get_json_data():
    response = requests.get(server+snapshots_path)
    if (response.status_code >= 200 and response.status_code <= 299):
        return json.loads(response.text)['snapshotItems']
    else:
        print(f'Response code: {response.status_code}')
        exit(1)

def list_all_by_DB():
    snapshots={}
    json=get_json_data()
    time_sorted_snaps = sorted(json, key=lambda x: dt.strptime(x[creation], time_format), reverse=True)
    for obj in time_sorted_snaps:
        db=obj[databaseName]
        if not db in snapshots:
            snapshots[db]=[]
        snapshots[db].append(obj)
    return snapshots

def do_by_id(id,method):
    if(method=='GET'):
        response = requests.get(server+snapshots_path+str(id))
        if (response.status_code >= 200 and response.status_code <= 299):
            print(response.text)
            return True
        else:
            print(f'Response code: {response.status_code}')
    elif (method=='DELETE'):
        response = requests.delete(server+snapshots_path+str(id))
        if (response.status_code >= 200 and response.status_code <= 299):
            return True
        else:
            print(f'Response code: {response.status_code}')

def main(argv):
    global server
    server = argv[1]            #'https://5dbf2fb9e295da001400b4cc.mockapi.io'
    global snapshots_path
    snapshots_path = argv[2]    #'/api/v1/snapshots/'
    all_snaps=list_all_by_DB()
    for db_name in all_snaps:
        db=all_snaps[db_name]
        if len(db) > 2:
            i=1
            for snap in db[2:]:
                do_by_id(int(snap['id']),'DELETE')

    print("done")
if __name__ == '__main__':
    main(sys.argv)