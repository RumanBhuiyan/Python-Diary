"""
is-a-relationship => As child class inherits parent class , all attributes,methods come into child class from parent class
has-a-relationship => if we create an instance of parent class inside constructor of child class instead of inheriting parent class
                        then we can utilise the value what we need from that instance. Here we don't need to take unneccessary 
                        attributes,methods from parent class to child class which come due to inheriting.

composition concept is nothing but has-a-relationship
"""

class Student:
    def __init__(self,name,roll,cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    
    @property
    def get_name(self):
        return self.name
    
    @property
    def get_roll(self):
        return self.roll
    
    @property
    def get_cgpa(self):
        return self.cgpa


# if we inherit Student class here then get_name() will come inside BrilliantStudents. But we dont need this method
# for this class so instead of inheriting it lets make an object of that class inside constructor and use the
# only property,attribute,method that we need
class BrilliantStudents:

    brilliants = dict()

    def __init__(self,name,roll,cgpa):
        self.student = Student(name, roll, cgpa)

        if self.student.get_cgpa >= 3.75:
            BrilliantStudents.brilliants[self.student.get_roll] = self.student.get_cgpa

_ = BrilliantStudents('student1', 3, 3.81)
_ = BrilliantStudents('student2', 1, 3.25)
_ = BrilliantStudents('student3', 4, 3.94)
_ = BrilliantStudents('student4', 2, 3.87)

print(BrilliantStudents.brilliants)
