import json 

# converting a JSON object into a Python object is called deserialization.
# We can do this using the methods json.loads() and json.load()
# json.loads() is used to deserialise from a object of current python file
# json.load() is used  to deserialise from json file

with open('person_data.json','r') as json_file:
    person_dict = json.load(json_file)
    print(person_dict)