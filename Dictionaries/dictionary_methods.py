"""
    dictionaries are called as map, hashmap, lookup table, associative aray which are 
    built in using hash-table which takes O(1) time to insert,update,delete 

    N.B => each dictionary key will have to be unique otherwise hash of two same key will conflict 
    inside that dictionary that's why immutable objects should be used as dictionary like string,
    tuple etc. string,tuple values wont be change in whole lifetime. If you go to use list as a
    ditionary key then python will throw en error informing that unhashable object can't be used as key.
"""


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


# if we try to acccess a key like words['bio'] that doesn't exist in dictionary it throws an error
# but if we access any key's value like words.get('bio') then no error is thrown rather returns falsy value None
print(a.get('one'))
print(a.get('five'))