# takin input & storing into a variable
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number:  '))
# printing output
print('The summation is ', (num1+num2))
# String interpolation or formating
print(f'The numbers are {num1} {num2}')
print('The numbers are {0} {1}'.format(num1, num2))
print('The numbers are {1} {0}'.format(num1, num2))
print('The numbers are {a} {b}'.format(a=num1, b=num2))
print('The summation is '+str((num1+num2)))  # type casting

# in python there is no need to say datatype explicitely
a = 1
b = 'Ruman'
c = 24.5
d = True
print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)
# Arithmetic operations with their operators
a = 6
b = 2
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# python is dynamically typed language not statically typed language
# dynamically typed menas if a variable holds int type value later it can
# hold string type float type values too. but statically type can't do it
