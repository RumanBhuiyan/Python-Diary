class Person:

    def __init__(self,firstname,lastname,age,NID) :
        # public variables
        self.firstname = firstname
        self.lastname = lastname

        # according to PEP 8, _age this type variables indicates for internal use
        # variable_ is used when variable name conflicts with python keyword then 
        # additional _ after keyword will inform python interpreter to ignore this 
        # protected variable (with single underscore)
        self._age = age

        # private variable (with double underscore)
        self.__NID = NID
    
    # getter method : process : 01
    def get_firstname(self):
        return self.firstname

    # getter method  : process : 02
    @property
    def age(self): # self bind this method to instance or object of this class
        return self._age

    # setter method : process : 01
    def set_firstname(self,name):
        self.firstname = name
    
    # setter method : process : 02
    @age.setter
    def age(self,value):
        self._age = value


ruman = Person('Ruman','Bhuiyan',23,123456)

# accessing getter methods 
print(f'First Name : {ruman.get_firstname()}')
print(f'Age : {ruman.age}')

# accessing setter methods
ruman.set_firstname('Max')
ruman.age = 24
print(f'First name : {ruman.firstname}')
print(f'Age : {ruman.age}')


# getter setter using getattr() and setattr()
# scenario : 01 (working with non-existing attribute)

# add an attribute named Nationality with value Bangladeshi to this object
setattr(ruman,'Nationality','Bangladeshi') 

# get object attribute value
nationality = getattr(ruman,'Nationality')
print(nationality)


# scenario  : 02 (working with existing attribute)
setattr(ruman,'firstname','William')
name = getattr(ruman,'firstname')
print(name)