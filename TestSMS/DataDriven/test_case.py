import requests
import json
import os
from DataDriven import library


def test_add_students_ddt_2():

    url = 'https://thetestingworldapi.com/api/studentsDetails'
    f = open('H:/Git_projekty/Api using python/TestSMS/add_student_ddt.json', 'r')
    json_request = json.loads(f.read())
    
    obj = library.Common(os.path.abspath('test_data.xlsx'), 'Arkusz1')
    col = obj.column_count()
    keyList = obj.key_names()
    row = obj.row_count()
    
    for i in range(2, row+1): 
        update_json_request = obj.update_request_with_data(i, json_request, keyList)
        response = requests.post(url, update_json_request)
        print(response)
        
        