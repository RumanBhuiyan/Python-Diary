import json

# python dictionary
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# open file then convert person to json then write json into json file
with open('person_data.json','a') as file:
    json.dump(person,file,indent=4)

#N.B
# json.dump() can convert python dict to JSON & write into file but
# json.dumps() can only convert python dict to JSON , it can't write into file