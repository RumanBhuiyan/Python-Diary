# conditional statements
operator = input('Enter the operator +,-,*,/,%: ')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
# if-elif-else block
if operator in ['+', '-', '*', '/', '%']:
    if(operator == '+'):
        print(f"Summation is {num1+num2}")
    elif(operator == '-'):
        print(f"Subtraction is {num1-num2}")
    elif(operator == '*'):
        print(f"Product is {num1*num2}")
    elif(operator == '/'):
        print(f"division is {num1/num2}")
    else:
        print(f'Remainder is {num1%num2}')
else:
    print('Enter the correct operator please!!')

# ternay operator
print('num1 is', 'Positive' if num1 >= 0 else 'Negative')
