# method starts and ends with __ are called dunder(short of Double underscore) methods or magic methods
# () after class name is option in class declaration

# Sequence of calling
'''' 
     __str__() or str()
            ⬇️
     __repr__() or repr()
            ⬇️
     python in-built __repr__() or repr()
'''

class Person:
    def __init__(self,name):
        self.name = name    
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Person(name : {self.name})'
    
    def print_self(self):
        # self also follows the order of above
        print(self)


p1 = Person('Elon')

# call __repr__() implementation of Person class
# missing __repr__() -> call inbuilt repr() or __repr__()
print(p1.__repr__())
print(repr(p1))

# call __str__() implementation of Person class
# missing  __str__()  -> call __repr__()
# missing  __repr__() -> call inbuilt __repr__()
print(p1.__str__())
print(str(p1))

# calls __str__() implementation of Person class
# missing __str__()   -> call __repr__().
# missing __repr__()  -> call inbuilt repr() or __repr__()
print(p1)

# calls __str__() implementation of Person class
# missing __str__()   -> call __repr__().
# missing __repr__()  -> call inbuilt repr() or __repr__()
p1.print_self()