# list has .reverse() method but strings hasn't .reverse() so
# in that case use  reversed()
numbers = [1,2,3,4,5]
another = numbers

numbers.reverse()
print(numbers)
print(list(reversed(another)))

# reversing a string
print(list(reversed('hello')))