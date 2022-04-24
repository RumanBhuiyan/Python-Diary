class Person:
    # class vairables or resources
    # track is Person class resource where every object of this class will have access to this resource
    track = []
    even_numbers = [100, 200, 300, 400]
    
    def __init__(self,init):
        # Object variables or resources
        self.object_counter = init
        self.even_numbers = [2, 4, 6, 8]

        if self.object_counter %2 == 0:
            Person.track.append(self.object_counter)
    
    @classmethod
    def show(cls):
        # access of cls comes from @classmethod 
        print(f'Person class track : {cls.track}')


p1 = Person(1)
p2 = Person(2)
p3 = Person(3)
p4 = Person(4)

# As track isn't shadowed in object constructor so both Person and p1 points the same track
Person.show()
print(f'p1 track : {p1.track}')

# Becuase of  shadowing even_numbers in object constructor, Person and p1 point different even_numbers
print(f'Person class even_numbers : {Person.even_numbers}')
print(f'Object even_numbers : {p1.even_numbers}')