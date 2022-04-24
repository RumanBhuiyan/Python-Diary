class Person:

    '''N.B : in case of creating getter, you can give any name to that function but 
    same function name will have to be used in setter and deleter
    ''' 

    def __init__(self):
        self._age = 24
        self.fname = 'ruman'
        self.lname = 'bhuiyan'

    # process - 01 : creating getter, setter, deleter using same name of variable
    # to avoid confliction withing function name age and self.age make your variable
    # protected like self._age
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
    
    @age.deleter
    def age(self):
        print('deleted age attribute')
        del self._age

    # process -02 : creating getter, setter, deleter using different name of function
    @property
    def fullname(self) :
        return f'{self.fname} {self.lname}'
    
    @fullname.setter
    def fullname(self,full_name):
        self.fname, self.lname = full_name.split(' ')
    
    @fullname.deleter
    def fullname(self):
        del self.fname
        del self.lname
        print('fname and lname deleted')



p = Person()

print(p.age)
p.age = 36
print(p.age)
del p.age

print(p.fullname)
p.fullname = "Elon musk"
print(p.fullname)
del p.fullname
