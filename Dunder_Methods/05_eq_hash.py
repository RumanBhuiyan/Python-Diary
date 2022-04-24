"""
    __eq__() checks equality when object1 == object2 is called
    __hash__() generates hash for class object
"""

class Person:
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        print(f'{self.name} __eq__() is called')

        if not isinstance(other, Person):
            raise Exception(f"{other} isn't object of Person")

        return self.name == other.name
    
    # id(object) returns the memory location of that object which is unique for all object
    # and an excellent choice for creating hash from this.
    def __hash__(self):
        # to be sure that Person class __hash__ is called not python in-built hash()
        print(f'Person class __hash__ is called')
        return id(self)


person1 = Person('Ruman')
person2 = Person('Ruman')

print(f'{person1 == person2}')
# print(f'{person1 == "ruman"}') # throws error 

# creating hash 
print(f'Hash of person1 : {hash(person1)}')
print(f'Hash of person2 : {hash(person2)}')
