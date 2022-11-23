import requests
import json
import jsonpath
import os
import pytest

# nowy zasób na serwerze
url = "https://reqres.in/api/users"

@pytest.fixture(scope='module')
def start_exec():
    global file
    global requests_json
    file = open(os.path.abspath('plik.json'), 'r')
    json_input = file.read()
    requests_json = json.loads(json_input)

@pytest.mark.Smoke
def test_create_new_users(start_exec):
    response = requests.post(url, requests_json)
    assert response.status_code == 201, 'To nie jest 201'

@pytest.mark.Sanity
def test_create_other_users(start_exec):
    response = requests.post(url, requests_json)
    response_json = json.loads(response.text) 
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0]) 