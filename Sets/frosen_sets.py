# article resource : https://www.askpython.com/python/built-in-methods/python-frozenset
# A frozenset is an unordered, un-indexed, and immutable collection of elements.
# It provides all the functionalities that a set offers in Python, the only difference
# being the fact that a frozenset is immutable, i.e. can’t be changed after it is created.
# Hence in simple words, frozen sets are immutable sets.
# Consider in our program we are using a mutable object like List but, 
# after a certain point in our program we do not want any user to change or modify it. 
# We are kind of warning the person reading the code that we do not have to modify this further in the program.
#  In such cases, Frozensets can help us.

# make frozenset from list
my_list = [1,2,3,4,5]
print(f'Frozenset from list : {frozenset(my_list)}')

# make frozenset from tuple
my_tuple = (1,2,3,4,5)
print(f'Frozenset from tuple : {frozenset(my_tuple)}')

# make frozenset from dictionary
my_dict = { 'one' : 1 , 'two' : 2 , 'three' : 3}
print(f'Frozenset from dictionary : {frozenset(my_dict)}')

# make frozenset from set 
my_set = {1,2,3,4,5}
print(f'Frozenset from set : {frozenset(my_set)}')

# checking avaiable methods of frozenset using dir() 
print(dir(frozenset(my_list)))

fs = frozenset([1, 12, 23, 45, 67, 89, 100])
 
print("Given Frozenset =", fs)
 
fs_len = len(fs)
print("Length of Frozenset =", fs_len)
 
print("23 in fs? ", 23 in fs)
 
print("23 not in fs? ", 23 not in fs)
 
print("Sets are disjoint? ", fs.isdisjoint(frozenset([10, 5])))
 
print("Set is Subset? ", fs.issubset(set([1, 2, 3, 4, 12, 23, 45, 67, 89, 100])))
 
print("fs is superset? ", fs.issuperset(frozenset({1, 100})))
 
print("Union of sets: ", fs.union(frozenset([-1, -12])))
 
print("Intersection: ", fs.intersection(set([1, 10, 100])))
 
print("Difference: ", fs.difference(frozenset([1, 10, 100])))
 
print("Symmetric difference: ", fs.symmetric_difference(frozenset([1, 10, 100])))
 
fs_copy = fs.copy()
print("Copy of fs: ", fs_copy)