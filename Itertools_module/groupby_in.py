from itertools import groupby

a = [1,2,3,4,5]

# groupify items basis on a key passed in key parameter
keep = groupby(a,key=lambda x : x < 3)

for key , value in keep :
    print(f'{key} {list(value)}')

# output : 
# True [1, 2]
# False [3, 4, 5]
