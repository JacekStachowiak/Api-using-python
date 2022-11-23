import requests
import json
import jsonpath
import os

# nowy zasób na serwerze
url = "https://reqres.in/api/users/2" # konkretny element

file = open(os.path.abspath('..\\API_automation\\plik.json'), 'r')
json_input = file.read()
requests_json = json.loads(json_input) 

print(requests_json) # {'name': 'Testing World Updatet', 'job': 'Trainer : testingworldindia@gmail.com updatet'}

response = requests.put(url, requests_json)
print(response.content)     # b'{"name":"Testing World Updatet","job":"Trainer : testingworldindia@gmail.com updatet","updatedAt":"2022-11-19T19:58:25.968Z"}'
print(response.status_code) # 200

assert response.status_code == 200, 'To nie jest 200'
response_json = json.loads(response.text)
print(response_json)  # {'name': 'Testing World Updatet', 'job': 'Trainer : testingworldindia@gmail.com updatet', 'updatedAt': '2022-11-19T20:01:28.596Z'}
updated = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated[0]) # 2022-11-19T20:05:36.073Z
