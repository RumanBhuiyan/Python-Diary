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

# access values of tuple by name
print(f"Name : {ruman.name} regno : {ruman.regno} department : {ruman.department}")

# access values of tuple by index
print(f"Name : {ruman[0]} regno : {ruman[1]} department : {ruman[2]}")

# As python generates Examinee class for us under the hood so we can inherit this class to add methods
class ExamineeFacilities(Examinee):
    def get_regno(self):
        return self.regno

e = ExamineeFacilities('robiul',201631079, 'CSE')
print(e)
print(e.get_regno())
