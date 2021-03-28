# map , filter functions
numbers = [1, 2, 3, 4, 5]

def square(num):
    return num**2

# using map function with named function
squareNumbers = list(map(square, numbers))
print(f'Square of Numbers : {squareNumbers}')
# using map function with anonymous or lambda function
cubeNumbers = list(map((lambda num: num**3), numbers))
print(f'Cube of numbers: {cubeNumbers}')

def even(num):
    return num % 2 == 0

# using filter function with named function
evenNumbers = list(filter(even, numbers))
print(f'Even Numbers: {evenNumbers}')
# using filter function with anonymous of lambda function
oddNumbers = list(filter(lambda num: num % 2, numbers))
print(f'Odd Numbers: {oddNumbers}')

# map function returns items performing operation on each but
# filter function return those item which satisfy the condition
