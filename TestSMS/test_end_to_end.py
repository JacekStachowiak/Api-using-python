import requests
import json
import jsonpath
import os

def test_add_new_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open(os.path.abspath('data1.json'), 'r')
    requests_json = json.loads(file.read())
    response = requests.post(url, requests_json)
    print(f'Post student_2: {response.text}')   # Post student_2: {"id":3937622,"first_name":"testing","middle_name":"M","last_name":"World1","date_of_birth":"11/11/2000"}
    id = jsonpath.jsonpath(response.json(), 'id')
    print(f'Id studenta_2: {id[0]}')    # Id studenta_2: 3937624
    
    
    # dopisujemy do technicalskills --> umiejętnosci
    tech_url = 'https://thetestingworldapi.com/api/technicalskills'
    file = open(os.path.abspath('data_tech.json'), 'r')
    requests_json = json.loads(file.read())
    requests_json['id'] = int(id[0])
    requests_json['st_id'] = id[0]
    response = requests.post(tech_url, requests_json)
    print(f'Post student_2_tech: {response.text}')  # student_2_tech: {"status":"true","msg":"Add  data success"}
    
    
    # dopisujemy do addressów
    address_url = 'https://thetestingworldapi.com/api/addresses'
    file = open(os.path.abspath('data_address.json'), 'r')
    requests_json = json.loads(file.read())
    requests_json['stId'] = id[0]
    response = requests.post(address_url, requests_json)
    print(f'Post student_2_address: {response.text}')  # student_2_address: {"status":"true","msg":"Add  data success"
    
    
    # pobieramy komplet danych studenta
    final_url = 'https://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response = requests.get(final_url)
    print(response.text)