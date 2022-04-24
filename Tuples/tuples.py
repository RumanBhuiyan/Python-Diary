# tuples are similar as list but the difference is
# tuples items are immutable and access time is faster than list
# dict.items() returns a tuple thats why you can use tuple as a key
# in dictionary but you can't list in this case

# creating tuple 
month_index = (0,1,2,3,4,5,6,7,8,9,10,11)
months = ('January','February','March','April','May','June','July','August'
    ,'September','October','November','December','whatever')

# accessing tuple items
for id in month_index:
    print(f'{id +1} month = {months[id]}')

# creating a dictionary to get it items as tuple
numbers_identity = {'1':'odd','2':'Even', '3':'Odd','4':'even'}

for item in numbers_identity.items():
    print(item)

# there are 2 methods of tuple count and index
print(f'2 is {month_index.count(2)} times')
print(f'index of 3 is {month_index.index(3)}')