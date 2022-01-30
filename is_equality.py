a = [1,2,3,4,5]
b = a # b and a is pointing same object thats why a==b is True & a is b is also True
c = list(a) # c points to different memory location thats why a is not c

print(f'a == b : {a == b}')
print(f'a is b : {a is b}')
print(f'c == a : {c == a}')
print(f'c is a : {c is a}')

# N.B:
# == checks whether two object contains same contents/items or not
# is checks whether two objects points same memory location or not