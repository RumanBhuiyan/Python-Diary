"""
    var__
    function__
    variable and function name ends with __ double underscore has no difference or special meaning. Those are
    treated as general object variables and methods. But 

    __var__
    __function__
    those type of practises are bad because they can conflict with python built-in functions or keywords.
    So we shouldn't use them
"""
class Person:
    def __init__(self,name):
        self.name = name
        self.counter__ = 25
    
    def get_counter__(self):
        return self.counter__
    


ruman = Person('Ruman')

print(ruman.counter__)
print(ruman.get_counter__())