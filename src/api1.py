# -*- coding: utf-8 -*-
"""
Spyder Editor
wK1GEkdftBZC0YqL1kuaeH7Tx
This is a temporary script file.
"""

import os
import json 
from sodapy import Socrata
def api(page_size,num_pages,output_fn):
    APP_KEY=os.environ.get('APP_KEY')
    client = Socrata("data.cityofnewyork.us",APP_KEY)
    for i in range(num_pages):
        ncdata=client.get("nc67-uf89",limit=page_size,offset=page_size*i)
        with open(output_fn,'a') as fw:
            print(ncdata)
            output=json.dumps(ncdata)
            fw.write(output+'\n')

