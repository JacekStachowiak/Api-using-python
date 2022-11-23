import json

# http://jsonpath.com/
# można skopiować swojego json-a - wkleić
# parse dictionary to json  and json to dictionary

dictionary = '{"k1":"val1","k2":"val2"}' # słownik jako łańcuch --> muszą być "" - nie odwrotnie
json_result = json.loads(dictionary)  # słownik parsowany na formay json

print(json_result)          # {'k1': 'val1', 'k2': 'val2'}
print(json_result['k1'])    # val1


 