"""
    == operator checks whether two objects content are same or not
    is operator checks whether two objects point same memory location or hold same reference or not
"""

# b and a is pointing same object thats why a==b is True & a is b is also True
# c points to different memory location thats why a is not c
a = [1,2,3,4,5]
b = a 
c = list(a) 

print(f'a == b : {a == b}') # True
print(f'a is b : {a is b}') # True
print(f'c == a : {c == a}') # True
print(f'c is a : {c is a}') # Flase

# N.B:
# == checks whether two object contains same contents/items or not
# is checks whether two objects points same memory location or not