# map function takes 2 argument. function and iterable object like list,tuple,set,
# dictionary and perform an operation on each item of that iterable object that is told
# to do in lambda function and return new items
numbers = [1,2,3,4,5,6]

def triple(x):
    return x*3

doubles = map(lambda x:x*2,numbers)
triples = map(triple,numbers)

def print_items(numbers):
    for num in numbers:
        print(num)

print_items(doubles)
print_items(triples)