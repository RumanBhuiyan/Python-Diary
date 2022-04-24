"""
    __call__ dunder methods implementation and binding it with self keyword makes our objects callable
    like below
"""
class Person:
    def __init__(self,name):
        self.name = name
    
    def __call__(self):
        print(f'So you are {self.name}')
    

ruman = Person('Ruman')

# this will invoke the __call__() or Person class as ruman is object of Person class
ruman()