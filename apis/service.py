from settings import BASE_URL, JSON_HEADERS, MULTIPART_HEADERS
import json
import requests
import os

class Service():
    def __init__(self):
        pass
    
    def login(self, username, password):
        if username and password:
            try:
                json_data = json.dumps({"username": username, "password": password})
                query_url = BASE_URL+'/core/api/token/'
                response = requests.post(query_url, json_data,
                                    headers=JSON_HEADERS)
                print(response.json())
                return response
            except Exception as e:
                print(e)
                
    def post_worker(self, worker_name, ip_address, user_id, city=None, region=None, country=None):
        if ip_address:
            try:
                json_data = json.dumps({"name": worker_name ,"user": user_id, "is_alive": "True", "ip_address": ip_address, "city": city, "region": region, "country": country})
                query_url = BASE_URL+'/core/api/worker/'
                response = requests.post(query_url, json_data,
                                    headers=JSON_HEADERS)
                print(response.json())
                if response.status_code == 201:
                    return response.json()
                else:
                    return None
            except Exception as e:
                print(e)

    def put_worker(self, worker_id, worker_name, ip_address, city=None, region=None, country=None):
        if ip_address:
            try:
                json_data = json.dumps({"name": worker_name ,"is_alive": "True", "ip_address": ip_address, "city": city, "region": region, "country": country})
                query_url = BASE_URL+'/core/api/worker/{}/'.format(worker_id)
                response = requests.put(query_url, json_data,
                                    headers=JSON_HEADERS)
                print(response.json())
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except Exception as e:
                print(e)
                
    def get_worker(self, user_id):
        if user_id:
            try:
                query_url = BASE_URL+'/core/api/worker/user/{}/'.format(user_id)
                response = requests.get(query_url,
                                    headers=JSON_HEADERS)
                print(response.json())
                if response.status_code == 200:
                    return response.json()
                else:
                    return None
            except Exception as e:
                print(e)
                
    def version(self, worker_id):
        if worker_id:
            try:
                json_data = json.dumps({"workers": [worker_id]})
                query_url = BASE_URL+'/core/api/version/'
                response = requests.post(query_url, json_data,
                                    headers=JSON_HEADERS)
                print(response.json())
                return response.json()
            except Exception as e:
                print(e)
            
                
    def handle_version(self, version_id, worker_id):
        if version_id and worker_id:
            try:
                query_url = BASE_URL+'/core/api/handle_version/{}/{}/'.format(version_id, worker_id)
                response = requests.post(query_url,
                                    headers=JSON_HEADERS)
                print(response.json())
                return response.json()
            except Exception as e:
                print(e)
            
    def query_file(self,version_id, handle_id, query_file_name):
        try:
            data = {'version_id': version_id, 'handle_id': handle_id}
            files = {'query_file': open('avro_files/collections/' + query_file_name, 'rb')}
            query_url = BASE_URL+'/core/api/query_file/'
            response = requests.post(query_url, files=files, data=data)
            print(response.json())
            if response.status_code == 200:
                print('Query file uploaded successfully')
                os.remove(os.path.join('avro_files/collections/', query_file_name))
        except Exception as e:
            print(e)