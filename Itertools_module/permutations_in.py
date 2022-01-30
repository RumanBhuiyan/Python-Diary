from itertools import permutations

a = [1,2,3]

# show all possible arrangements of 1,2,3 of default len(a)
print(list(permutations(a))) 
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# show all possible arrangements of 1,2,3 of length 2
print(list(permutations(a,2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]