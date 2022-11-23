import requests
import json
import jsonpath
import os

def test_add_new_student():
    global id
    url = 'https://thetestingworldapi.com/api/studentsDetails'
    f = open(os.path.abspath('add_student.json'), 'r')
    requests_json = json.loads(f.read())
    response = requests.post(url, requests_json)
    print(f'Post add_student: {response.text}')  # Post add_student: {"id":3937631,"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"07/01/1964"}
    id = jsonpath.jsonpath(response.json(), 'id')
    print(f'Id add_studenta: {id[0]}')  # Id add_studenta: 3937635
    

def test_get_details():
    get_url = f'https://thetestingworldapi.com/api/FinalStudentDetails/{str(id[0])}' 
    response = requests.get(get_url)
    print(response.text)  # {"status":"true","data":{"first_name":"Testing","middle_name":"K","last_name":"World","date_of_birth":"07/01/1964","TechnicalDetails":[],"Address":[]}}
    
    
        