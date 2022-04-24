# lets look at list unpacking
a = [1,2,3,4,5]

b = [*a,6,7,8] # this unpacking features exists in python 3 not in python 2
c = a[0:] + [6,7,8] # string slicing available in both python 2 and 3
a.clear() # this doesn't affect b & c that means b,c got copy of a not reference of a

print(f'a: {a}')
print(f'b: {b}')
print(f'c: {c}')


# lets look at dictionary unpacking
person = { "name" : "Ruman", "age" : 23} 
person2 = {**person , "profession" : "student"} 
person.clear() # this wont affect person2

print(f'person {person}')# person {}
print(f'person2 {person2}')#person2 {'name': 'Ruman', 'age': 23, 'profession': 'student'}


# lets look another example of unpacking
numbers = [1,2,3,4,5,6]
first,*middle,last = numbers

print(first) # 1
print(middle) # [2,3,4,5]
print(last) #6