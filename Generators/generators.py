# generators are subset of iterator
# every generator is an iterator but every iterator is not a generator
def count_upto(target):
    number = 1
    while number <= target:
        yield number
        number += 1

print(count_upto(10)) # <generator object count_upto at 0x0000021B2E14AB30>
print(list(count_upto(10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#help(count_upto(10)) # look python created __next__() for this generator

counter = count_upto(5)
print(next(counter)) # this will call __next__() of count_upto() generator
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

for number in count_upto(10):
    print(number)

# that means python pre-built for loop uses generator under the hood
# if you have to do repetitive task & you dont need to store previous value
# then use generator because it takes only one unit of memory and saves your
# memory and time also. generator doesn't take memory at first rather it takes
# memory at run time and free up memory after calculation


# generator comprehension or short hand
squares = (num**2 for num in range(10))
for number in squares:
    print(number)