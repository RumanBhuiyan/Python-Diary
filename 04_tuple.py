# tuple is simmillar as list but the difference is
# tuple immutable & faster than list but pop(),remove()etc absent in tuple
names_tuple = ('Ruman', 'Robiul', 'Ontor', 'Parbez', 'Shahadat')

print("At the beginning: ", names_tuple)
print('Second item: ', names_tuple[1])
# its not valid ->names_tuple[1] = 'Sany' because tuple is immutable

# adding items to tuple:
names_tuple = names_tuple + ('sany',)
print("After new item: ", names_tuple)
print("converting to list: ", list(names_tuple))

# tuple unpacking: == Destructuring in javascript
nameList = [(1, 'Ruman'), (2, 'Robiul'), (3, 'Shahadat'), (4, 'Ontor')]
for index, name in nameList:
    print(f'{index}: {name}')

for eachName in nameList:
    print(f'{eachName[0]} : {eachName[1]}')
