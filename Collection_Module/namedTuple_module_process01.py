from collections import namedtuple

# if we use namedtuple we dont have to keep in mind index of tuple item
# rather we can access each item by key
# namedtuple is just like structure of c/c++
# namedtuple(name_of_tuple/structure_name,'field_names')

# create a class name Examinee and its fields are name, regno, department
# Examinee = namedtuple('Examinee','name,regno,department')
Examinee = namedtuple('Examinee',['name','regno','department'])

ruman  = Examinee('Ruman',2016331076,'CSE')

print(ruman)
print(f"Name : {ruman.name} regno : {ruman.regno} department : {ruman.department}")

