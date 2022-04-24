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

    def get_nid(self):
        return self.__NID
    
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

# throws error becuase private variables aren't accessible
# print(ruman.__NID)
print(ruman.get_nid())

# accessing getter methods 
print(f'First Name : {ruman.get_firstname()}')
print(f'Age : {ruman.age}')

ruman.set_firstname('Max')
ruman.age = 24

# accessing setter methods
print(f'First name : {ruman.firstname}')
print(f'Age : {ruman.age}')