# lambda function
def square(x): return x*x
def cube(x): return x*x*x


print(f'Square of 2: {square(2)}')
print(f'Cube of 2 : {cube(2)}')
# list comprehension in single loop


def myfunc(num):
    return num % 2 == 0


numbers = [num for num in range(1, 6)]
doubles = [num*2 for num in numbers]
evenNumbers = filter(myfunc, numbers)
# filter return those item which evaluation is true,if x true return it
oddNumbers = filter(lambda x: x % 2, numbers)

print(f'Double numbers: {doubles}')
print(f'Even numbers: {list(evenNumbers)}')
print(f'Odd numbers: {list(oddNumbers)}')
