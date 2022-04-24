# article resource : https://www.askpython.com/python-modules/python-json-module
# https://www.programiz.com/python-programming/json
import json

# convering JSON -> python dictionary
#simle json
person =  '{ "name":"John", "age":30, "city":"New York"}'
#convert json to python dictionary
person_dict=json.loads(person)
print(person_dict)

# converting Python dictionary -> JSON
# simple python dictionary
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# You can think of dumps() as serializing the Python object into a  JSON object and returning a string. 
# This is needed if you wish to transfer data across the internet.
#convert dictionary to json, indent 4 makes keys readable for us
x_json = json.dumps(x,indent=4,sort_keys=True)
print(x_json)
