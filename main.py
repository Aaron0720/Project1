import argparse
from time import sleep
from src.api1 import api


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--page_size',type=int)
    parser.add_argument('--num_pages',type=int,default=None)
    parser.add_argument('--output',default=None)
    parser.add_argument('--elastic',type=bool,default=False)
    args = parser.parse_args()


    api(args.page_size,args.num_pages,args.output,args.elastic)

    