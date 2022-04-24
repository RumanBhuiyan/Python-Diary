"""
    __variable
    __function
     wont come with objects and import statements but
    becuase of 'name mangling' those variables and methods are binded like 
    _<class_name>__<variable_name>, _<class_name>__<method_name> which we can find by dir(object_name)
    that's why we can change those variables value like _<class_name>__<variable_name> = <any_value>
    the way how python constructs name for variables, function started with __ is called name mangling.

    In my words, __var, __function are private variable and function
"""
class Person:
    def __init__(self, name):
        self.__age = 24
        self.name = name
    
    def __get_age(self):
        return self.__age
    
    def person_age(self):
        return self.__get_age();

    def get_name(self):
        return self.name


ruman = Person("Ruman")
abir = Person('Abir')

print(ruman.get_name())
# print(ruman.age) # throws error
# print(ruman.__get_age()) # throws error
print(ruman.person_age())

print(dir(ruman))

print(f'ruman age before change : {ruman._Person__age}')
ruman._Person__age = 25 # change age 
print(f'ruman age after change : {ruman._Person__age}') 
print(f'ruman age : {ruman._Person__get_age()}')

# N.B => changes in age of ruman object isn't reflected in abir object
print(f'abir age : {abir._Person__age}')