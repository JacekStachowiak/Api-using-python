# git hub api --> uwierzytelnianie podstawowe - login, hasło
import requests
from requests.auth import HTTPBasicAuth


def test_with_authentication():
    response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('testingworldnoida', '')) # --> users pokazuje otwarte
    print(response.text) 
    print(response.status_code) # 401
