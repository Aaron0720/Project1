import os
import json 
from sodapy import Socrata
from requests import get
from time import sleep
from datetime import datetime,date
from elasticsearch import Elasticsearch

APP_KEY=os.environ.get('APP_KEY')
client = Socrata("data.cityofnewyork.us",APP_KEY)

def create_and_update_index(index_name):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except:
        pass
    return es

def result_format(result):
    for key, value in result.items():
        if 'amount' in key:
            result[key] = float(value)
        elif 'date' in key:
            result[key] = datetime.strptime(result[key], '%m/%d/%Y').date()
        elif 'number' in key:
            result[key]=int(value)

def push_result(result, es, index):
    result_format(result)
    res = es.index(index=index, body=result,id=result['summons_number']) 



def api(page_size, num_pages, output,elastic):
    records = []
    rows = int(client.get('nc67-uf89',select='COUNT(*)')[0]['COUNT'])

    if not num_pages:
        num_pages = rows // page_size+1
    
    if elastic:
        es = create_and_update_index('nycvp')

    for i in range(num_pages):
        ncdata=client.get('nc67-uf89',limit=page_size,offset=page_size*i)
        for result in ncdata:
            with open(output,'a') as temp:
                temp.write(json.dump(result)+'\n')
            push_result(result,es,'nycvp')
    