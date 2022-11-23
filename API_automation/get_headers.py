import requests


# nowy zasób na serwerze
url = "https://httpbin.org/get" 
response = requests.get(url)
print(response.text)

print('='*30)
# dodaję nagłówek
headerdata = {'T1':'First_Header', 'T2':'Second_Header'}
response = requests.get(url, headers=headerdata)
print(response.text)