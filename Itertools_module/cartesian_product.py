from itertools import product

a = [1,2]
b = [3,4]

print(product(a,b)) # <itertools.product object at 0x0000027B89EA9140>
print(list(product(a,b))) # [(1, 3), (1, 4), (2, 3), (2, 4)]
# product() has an argument repeat where you can specify how many times it should repeat