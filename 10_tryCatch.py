num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number : '))

try:
    global result  # declaring global variable result
    result = num1 / num2
except:
    result = 0
    print('Invalid input')
finally:
    print(f'Quotient is ', result)
