from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

# show all combinations of length 2 of 1,2,3,4 here length parameter is must
print(list(combinations(a,2)))
#[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# show all combinations of length 2 of 1,2,3,4 including self replacement
print(list(combinations_with_replacement(a,2)))
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]