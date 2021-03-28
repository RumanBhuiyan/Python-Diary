import sys
# whenever a function get yield keyword it allocates 112 bytes of memory
# in memory  and stores value of local variable there.At the time of
# each iteration it calculates i**2 and return it & forgets previous i value

def sendGenerator(n):
    for i in range(1, n):
        yield i**2

# if you call sendGenerator(100000000)it will also take 112 bytes of memory
keep = sendGenerator(5)
print(sys.getsizeof(keep), ' bytes')
# you can't iterate over a generator more than once
# each iteration, loop sasy keep send me your next number like next(keep)
for num in keep:
    print(num, end=' ')
# now keep is empty thats why below line will generate empty list
print(f'\n{list(keep)}')

# creating generator in another way
numbers = (x**2 for x in range(1, 5))
print(type(numbers))

# iteration in another way
myIteration = iter(numbers)
print(next(myIteration), end=' ')
print(next(myIteration), end=' ')
print(next(myIteration), end=' ')
print(next(myIteration), end=' ')
