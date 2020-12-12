# to keep class body empty use the keyword 'pass'
class Biodata:
    age = 24
    # constructor, here self is reference to Biodata class like as 'this'
    # you can use any word instead of self here

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    # string representation of the class,self bind this method to object

    def __str__(self):
        return f'{self.name} is a {self.occupation}'
    # build your own function to return anything's length
    # thus you can build your ownkeyword to perform a task

    def __len__(self):
        return len(self.name)

    def showBiodata(self):
        print('Name : ', self.name, ' Occupation : ', self.occupation)


person = Biodata('Ruman', 'Engineer')
print('Person\'s age: ', person.age)
person.showBiodata()
print(f'String representation of the class is {str(person)}')
print(f'name\'s length: {len(person)}')
