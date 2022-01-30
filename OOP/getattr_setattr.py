class Person:
    pass


person_info = {'firstname': 'Ruman','lastname':'Bhuiyan'}

# setattr() is used as setter() of any class
for key,value in person_info.items():
    setattr(Person,key,value)


# getattr() is used as getter() of any class
for key in person_info.keys():
    print(getattr(Person,key))