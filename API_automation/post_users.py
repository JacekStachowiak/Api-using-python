import requests
import json
import jsonpath
import os

# nowy zasób na serwerze
url = "https://reqres.in/api/users"

file = open(os.path.abspath('..\\API_automation\\plik.json'), 'r')
json_input = file.read()
requests_json = json.loads(json_input) 

print(requests_json) # {'name': 'Testing World', 'job': 'Trainer : testingworldindia@gmail.com'}

response = requests.post(url, requests_json)
print(response.content)     # b'{"name":"Testing World","job":"Trainer : testingworldindia@gmail.com","id":"430","createdAt":"2022-11-19T13:49:32.599Z"}'
print(response.status_code) # 201

assert response.status_code == 201, 'To nie jest 201'

print(response.headers.get('Content-Length')) # 120
response_json = json.loads(response.text) # parsujemy na format json
print(response_json) # --> to samo co requests_json

id = jsonpath.jsonpath(response_json, 'id')
print(id[0]) 
