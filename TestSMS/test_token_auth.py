import requests
import json
import jsonpath

def test_api_auth():
    token_url = 'https://thetestingworldapi.com/Token'
    data = {'grant_type':'password', 'username':'admin','password':'....'}
    response = requests.post(token_url, data)
    print(response.text)   
    token_value = jsonpath.jsonpath(response.json(),'access_token')
    auth = {'Authorization':'Bearer '+token_value[0]}
    
    url = 'https://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(url, headers=auth)
    print(response.text)    # {"Message":"Authorization has been denied for this request."}
    
    
    
    
    