import requests


url = "https://reqres.in/api/users/2"
responce = requests.delete(url)     # zawsze dajemy do zmiennej
print(responce.status_code) # 204

assert responce.status_code == 204, 'To nie jest 204'
