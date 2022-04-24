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


ruman = Person('Ruman')

# print(ruman)
# print(ruman)
ruman.print_self()