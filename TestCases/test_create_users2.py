import requests
import json
import jsonpath
import os
import pytest

# nowy zasób na serwerze
url = "https://reqres.in/api/users"

a=101

@pytest.mark.skipif(a>10, reason='Test nie satysfakcjonujący')
def test_create_new_users():
    file = open(os.path.abspath('plik.json'), 'r')
    json_input = file.read()
    requests_json = json.loads(json_input) 
    response = requests.post(url, requests_json)

    assert response.status_code == 201, 'To nie jest 201'


def test_create_other_users():
    file = open(os.path.abspath('plik.json'), 'r')
    json_input = file.read()
    requests_json = json.loads(json_input) 
    response = requests.post(url, requests_json)
    response_json = json.loads(response.text) # parsujemy na format json
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0]) 