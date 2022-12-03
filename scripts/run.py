import json
import dns.resolver
import concurrent.futures
import sys
from datetime import datetime
import requests
import os
import glob

from crawler import CrawlerThread

if __name__ == '__main__':
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    handle_id = sys.argv[1]
    version_id = sys.argv[2]
    range_start = int(sys.argv[3])
    range_end = int(sys.argv[4])
    
    uncompleted_file = glob.glob('avro_files/collections/*.avro')
    
    if len(uncompleted_file) > 0:
        print('There is an uncompleted file, please check it')
        for file in uncompleted_file:
            os.remove(file)
    
    query_file_name = 'version_{}_handle_{}_{}.avro'.format(version_id, handle_id, datetime.now())
    
    today = datetime.now()
    domainList = []
    processedDomain = set()
    domainErrorDict = set()
    
    query_objects = []
    
    list_file = 'lists/top-1m.txt'
    
    crawler = CrawlerThread(handle_id=handle_id, query_file_name=query_file_name)
    
    with open(list_file, 'r') as f:
        lines = f.readlines()[range_start:range_end]
        for k in lines:
            sp = k.split(",") 
            domain = sp[1].strip()
            domainList.append(domain)
            
    for domain in domainList:
        if domain not in processedDomain:
            processedDomain.add(domain)
            query_objects.append(crawler.start(domain))
            
            
    try:
        data = {'version_id': version_id, 'handle_id': handle_id}
        files = {'query_file': open('avro_files/collections/' + query_file_name, 'rb')}
        query_url = 'http://localhost:8000/core/api/query_file/'
        response = requests.post(query_url, files=files, data=data)
        if response.status_code == 200:
            print('Query file uploaded successfully')
            os.remove(os.path.join('avro_files/collections/', query_file_name))
    except Exception as e:
        print(e)

    
            
    