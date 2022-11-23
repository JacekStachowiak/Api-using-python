import requests

# tworzę listę parametrów
param = {'name':'testingworld', 'email':'testingworldindia@gmial.com', 'number':'+55 987 654 321'}

url = "https://httpbin.org/get"  
response = requests.get(url)
print(response.text)
# "url": "https://httpbin.org/get"

print('='*40)

url = "https://httpbin.org/get"  
response = requests.get(url, params=param)
print(response.text)
# "url": "https://httpbin.org/get?name=testingworld&email=testingworldindia%40gmial.com&number=%2B55+987+654+321"