
# example-01
counter = { num : num**2 for num in range(1,6)}
print(counter) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# example-02
names = ['one','two','three','four','five']
counter = { num+1:names[num] for num in range(5)}
print(counter) # {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# example-03 
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

keep  = dict(zip(keys,values))
myDict = { k:v for (k,v) in zip(keys, values)}  

print(keep) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(myDict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


