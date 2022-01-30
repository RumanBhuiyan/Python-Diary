from collections import ChainMap

# chainMap is used to merge 2 or more dictionary
# after merging dictionaries if any items value of any dictionary is changed
#  then chainMap dictionary items values are updated automatically
even = {0:'even',2:'even',4:'even'}
odd = {1:'odd',3:'odd'}
numbers = ChainMap(even,odd)

print(numbers)

even[0] = 'undefined'
print(f"Even dict : {even}") # Even dict : {0: 'undefined', 2: 'even', 4: 'even'}
print(f"numbers dict : {numbers}") # numbers dict : ChainMap({0: 'undefined', 2: 'even', 4: 'even'}, {1: 'odd', 3: 'odd'})

# you can add new dictionary using numbers.new_child(dict)
