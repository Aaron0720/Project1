# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:33:47 2020

@author: Yuki
"""
from sys import argv
from src import api1
if __name__=="__main__":
    input_fn = argv[1]
    try:
        output_fn=argv[2]
    except Exception:
        output_fn='output.txt'
    with open(input_fn,'r') as fh:
        for line in fh:
            line = line.strip('\n')
            page_size,num_pages = line.split(' ')
            page_size=int(page_size)
            num_pages=int(num_pages)
            api1.api(page_size,num_pages,output_fn)
    