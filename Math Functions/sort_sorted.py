from operator import itemgetter

numbers = [23,21,2,1,0]

print(f"Before sorting : {numbers}")

# sort() sorts the original array
# python uses timsort algorithm under the hood for sorting

numbers.sort()
print(f"After sorting : {numbers}")

# sorted() doesn't change the original array rather it returns a 
# sorted copy of original array
numbers = [23,21,2,1,0]
another = sorted(numbers)
print(another)
print(numbers)
print(sorted(numbers,reverse=True))

# sorting basis on a key
keep=[
    {'name':'rahat', 'roll':23},
    {'name':'topu', 'roll':103},
    {'name':'shifat', 'roll':1},
    ]
print(sorted(keep,key = lambda user : user['name']))
print(sorted(keep,key = lambda user : user['roll']))

# itemgetter function helps us to sort basis on a key like below
print(sorted(keep,key = itemgetter('name')))

# # sorting a dictionary basis on many criteria
# name_roll = {'rahat':23,'topu':103,'shifat':1}
# print('sorting on length: ',sorted(name_roll,key = len))
# print('sorting on keys : ',sorted(name_roll.keys()))
# print('sorting on values : ',sorted(name_roll.values()))

# print('sorting on keyname: ',sorted(name_roll,key = lambda item: item))
# print('sorting on key length : ',sorted(name_roll,key = lambda item: len(item)))
# print('sorting on key',dict(sorted(name_roll.items())))


