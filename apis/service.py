from settings import BASE_URL, NEW_HEADERS
import json
import requests

class Service():
    def __init__(self, worker):
        self.worker = worker

    def alive(self):
        try:
            json_data = json.dumps({"is_alive": "True"})
            query_url = BASE_URL+'/core/api/alive/{}/'.format(self.worker)
            response = requests.put(query_url, json_data,
                                headers=NEW_HEADERS)
            print(response.json())
        except Exception as e:
            print(e)
            
    def query(self, query_data):
        try:
            json_data = json.dumps(query_data)
            query_url = BASE_URL+'/core/api/query/'
            response = requests.put(query_url, json_data,
                                headers=NEW_HEADERS)
            print(response.json())
        except Exception as e:
            print(e)