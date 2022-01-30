# if only __str__ exists then __repr__ and __str__ both call __str__
# if only __repr__ exists then __repr__ and __str__ both call __repr__
# if both exists then __repr__ calls __str__ and __str__ calls __str__
class Person:
    # self binds methods and attributes to objects
    def __init__(self,name) :
        self.name = name
    
    def __repr__(self) :
        return f'__repr__ is calling you Mr {self.name}'
    
    def __str__(self) :
        return f'__str__ is calling you Mr {self.name}'


p = Person("Ruman")
# print() calls __repr__(representation) of this object and __repr__ calls __str__ itself
print(p) 
# here print() is  calling __str__(string representation) of p
print("{}".format(p))