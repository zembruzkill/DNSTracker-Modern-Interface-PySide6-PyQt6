import json
import dns.resolver
import concurrent.futures
import sys
from datetime import datetime
import requests
import os


from crawler import CrawlerThread

if __name__ == '__main__':
    today = datetime.now()
    domainList = []
    processedDomain = set()
    domainErrorDict = set()
    
    query_objects = []
    
    list_file = '/tranco.txt'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    crawler = CrawlerThread()
    
    with open(base_dir + list_file, 'r') as f:
        lines = f.readlines()
        for k in lines[:30000]:
            sp = k.split(",") 
            domain = sp[1].strip()
            domainList.append(domain)
            
    for domain in domainList:
        if domain not in processedDomain:
            processedDomain.add(domain)
            query_objects.append(crawler.start(domain))
            
            
    