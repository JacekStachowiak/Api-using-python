import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)
print(response) # bez treści --> tylko kod
print('-'*50)
print(response.content) # treść
print('-'*50)
print(response.headers) # nagłówki
print('-'*50)
print(response.status_code) #200

assert response.status_code == 200

print(response.headers)
print(response.headers.get('Date'))     # Fri, 18 Nov 2022 21:18:03 GMT 
print(response.headers.get('Server'))   # cloudflare
print(response.cookies)  # cookies --> RequestsCookieJar[]
print(response.encoding) # utf-8
print(response.elapsed)  # czas jaki upływa od zapytania do odpowiedzi --> 0:00:00.197605
print('-'*50)
json_response = json.loads(response.text) # parsujemy response to json
print(json_response)

pages = jsonpath.jsonpath(json_response, 'total_pages') # zwróci listę z jedną wartością (tu 2) --> 2 argumenty (zmienna parsowana, element z listy)
print(pages)  #[2] --> lista jeden element 2
print(pages[0]) #2
assert pages[0] == 2

body = response.json()
print(body)
print(f'Response body: {json.dumps(response.json(), indent=4)}')

first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name)       # ['Michael']
print(first_name[0])    # Michael
# II zapis
print(body['data'][0]['first_name']) # Michael

first_name2 = jsonpath.jsonpath(json_response, 'data[2].first_name') # 3 miejsce na liście
print(first_name2)       # ['Tobias']
print(first_name2[0])    # Tobias
# II zapis
print(body['data'][2]['first_name'])  # Tobias
print('--------------------------------------')

# jeżeli wszystkie
for i in range(0,6):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name[0]) 

# II zapis
print('=========================================')
for i in range(0,3):
    print(body['data'][i]['first_name'])    

    