import requests
import json
import jsonpath
import os

def test_add_student_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    file = open(os.path.abspath('data.json'), 'r')
    json_requests = json.loads(file.read())
    response = requests.post(url, json_requests)
    print(f'Post student: {response.text}') # {"id":3937582,"first_name":"testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1995"}


def test_get_student():
    url = 'https://thetestingworldapi.com/api/studentsDetails/3937582'
    response = requests.get(url)
    json_response = json.loads(response.text)
    # json_response = response.json() --> też ok
    # Get student: {"status":"true","data":{"id":3937582,"first_name":"testing","middle_name":"K","last_name":"World","date_of_birth":"12/12/1995"}}
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(f'Id studenta: {id[0]}') # Id studenta: 3937582
    
    assert response.status_code == 200
    assert id[0] == 3937582
        

def test_update_student_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails/3937582'
    file = open(os.path.abspath('data.json'), 'r')
    json_requests = json.loads(file.read())
    response = requests.put(url, json_requests)
    print(f'Post student: {response.text}')    # {"status":"true","msg":"update  data success"}  
    print(response.status_code) # 200

# aby sprawdzić czy zaktualizowano
def test_get_student_data():
    url = 'https://thetestingworldapi.com/api/studentsDetails/3937582'
    response = requests.get(url)
    json_response = response.json()
    print(json_response)
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(f'Id studenta: {id[0]}') 
    
    assert response.status_code == 200
    assert id[0] == 3937582    

# delete student
def test_delete_student():
    url = 'https://thetestingworldapi.com/api/studentsDetails/3937582'
    response = requests.delete(url)
    print(response.text)

    
def test_get_student_data_after_delete():
    url = 'https://thetestingworldapi.com/api/studentsDetails/3937582'
    response = requests.get(url)
    json_response = response.json()
    print(json_response)                # {'status': 'false', 'msg': 'No data Found'}
    id = jsonpath.jsonpath(json_response, 'data.id')
    print(f'Id studenta: {id[0]}') 
    
    assert response.status_code == 200
    assert id[0] == 3937582      