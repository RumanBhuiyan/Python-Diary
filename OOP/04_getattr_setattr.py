class Person:
    pass

person_info = {'firstname': 'Ruman','lastname':'Bhuiyan'}


# setattr() is used to set attribute with value for any class
for key,value in person_info.items():
    setattr(Person,key,value)

# create object and check its attributes value
p1 = Person()
print(dir(p1)[-len(person_info):])


# getattr() is used to get attibute value of any class
for key in person_info.keys():
    print(f'Key : {key}  Value : {getattr(Person,key)}')