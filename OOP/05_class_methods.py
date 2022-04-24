class Person:

    # this dictionary is shared among all objects of this class
    person_id_info = {'p1': 1, 'p2' : 2, 'p3':3}

    def __init__(self,name,age):
        # create two attribute and bind them to object/instance of this class
        self.name = name
        self.age = age
    
    # public method
    # when you call <object_name>.get_salary(self) then the reference of the object is assigned
    # to self thats why self can access the same resources that a object has. becuase of . after 
    # the name of object those things happends 
    def get_salary(self):
        salary = self.__calculate_salary()
        return salary

    # private method starts with double underscore 
    # protected method starts with single underscore
    def __calculate_salary(self):
        return 7000 if self.age <=25 else 10_000

p1 = Person('Ruman',24)

# accessing shared resources
print(Person.person_id_info)
print(p1.person_id_info)

# accessing public methods
print(f'salary : {p1.get_salary()}')