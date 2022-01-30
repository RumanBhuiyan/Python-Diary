class Person:

    # this dictionary is shared among all objects of this class
    person_id_info = {'p1': 1, 'p2' : 2, 'p3':3}

    def __init__(self,name,age):
        # create two attribute and bind them to object/instance of this class
        self.name = name
        self.age = age
    
    # public method
    def get_salary(self):
        salary = self.__calculate_salary()
        return salary

    # private method starts with double underscore 
    # protected method starts with single underscore
    def __calculate_salary(self):
        return 7000 if self.age <=25 else 10_000
    
    # declaring static method 
    # process : 01 (using @classmethod decorator)
    @classmethod
    def is_even(cls,number): # cls is binding this method to class not with object
        return number %2 == 0

    # process : 02 (using @staticmethod decorator)
    @staticmethod
    def is_odd(number):
        return number %2 !=0

p1 = Person('Ruman',24)

# accessing shared resources
print(Person.person_id_info)
print(p1.person_id_info)

# accessing public methods
print(f'salary : {p1.get_salary()}')


# accessing static methods
print(f'Is 2 even ?: {Person.is_even(2)}')
print(f'Is 1 odd ?: {Person.is_odd(1)}')