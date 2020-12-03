# to keep class body empty use the keyword 'pass'
class Biodata:
    age = 24
    # constructor, here self is reference to Biodata class like as 'this'
    # you can use any word instead of self here

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def showBiodata(self):
        print('Name : ', self.name, ' Occupation : ', self.occupation)


person = Biodata('Ruman', 'Engineer')
print('Person\'s age: ', person.age)
person.showBiodata()
