# dictionary are built in using hash-table which takes O(1) time to insert,update,delete
# creating dictionary using dict() constructor
# look : inside dict() constructor we are passing key value using = not :
months = dict(January='01',February= '02',March='03')
print(months)


words = {
    "name": 'Ruman',
     "email": 'rumanbhuiyansany@gmail.com',
      'age': 23,
    }

# add a new item into dictionary
words['profession'] = 'Software Engineer'

# accessing keys 
print(words.keys()) # dict_keys(['name', 'email', 'age', 'profession'])
# accessing values
print(words.values()) # dict_values(['Ruman', 'rumanbhuiyansany@gmail.com', 23, 'Software Engineer'])

# iterating dictionary process-01:
for key, value in words.items() :
    print(f'key : {key} value : {value}')

# iterating dictionary process-02:
for key in words.keys() :
    print(f'key : {key} value : {words[key]}')

# iterating dictionary process-03:
for value in words.values() :
    print(f' value : {value}')

# pop last item
words.popitem()
print(words) # {'name': 'Ruman', 'email': 'rumanbhuiyansany@gmail.com', 'age': 23}

# pop item by key
age = words.pop('age')
print(age)
print(words)

# adding another dictionary
bio = {'age': 23, 'job': 'software engineer'}
words.update(bio)
print(words)
# {'name': 'Ruman', 'email': 'rumanbhuiyansany@gmail.com', 'age': 23, 'job': 'software engineer'}


# merging 2 dictionaries  this technique is called unpacking and combining
a = { 'one':1,'two':2}
b = { 'three':3,'four':4}
combined_dict = {**a,**b}
print(combined_dict) # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
