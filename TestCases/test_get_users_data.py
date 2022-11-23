import requests
import json
import jsonpath
import pytest

@pytest.mark.Smoke
def test_user_details():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)

    assert response.status_code == 200
    json_response = json.loads(response.text) # parsujemy response to json
   
    for i in range(0,6):
        first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
        print(first_name[0]) 
  