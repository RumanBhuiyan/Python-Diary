class Numbers:

    # now friend_numbers list is shared list among all object of this class
    # any object of this class can access it by Numbers.friend_numbers
    friend_numbers = [121,131,141]


    def __init__(self,args):
        # declaring class public variable
        self.numbers = args
        Numbers.friend_numbers.append(151)

        # declaring protected variable
        self._age = 0

        # with single underscore we declare protected variable
        # with double underscore we declare private variable
        self.__password = '123456'
    
    # defining a getter method using @property decorator
    @property 
    def age(self):
        return self._age

    # defining a setter method using decorator
    @age.setter
    def age(self,value):
        self._age = value if value >= 0 else 0
    
    def print_numbers(self):
        print(self.numbers)
    
    # __repr__ returns the string representation of class attributes
    def __repr__(self) -> str:
        return f"class name is {__name__}"

    # static method
    # if we use @classmethod then we need to use cls in place of self
    @classmethod
    def get_myName(cls,name):
        return "Hello "+name;

    # process -02 of using static method
    @staticmethod
    def get_product(a,b):
        return a*b


keep = Numbers([1,2,3,4,5])
keep.print_numbers()
print(keep.friend_numbers)
print(Numbers.friend_numbers)

# str(keep) will call __repr__ method of that class
print(str(keep))

# look i am calling age getter method not _age property of that class
print(f"Before changing : {keep.age}")
keep.age = 24
print(f"After changing : {keep.age}")