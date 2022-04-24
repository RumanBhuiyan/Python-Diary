# eval(expression) executes any python expression and returns its result
# exec(python_code) executes any python code and returns its result

answer = eval(' 2 > 5')
print(answer)

my_code = '''
number = 5
if number % 2 == 0:
    print('Even number')
else:
    print('Odd Number')
 '''

exec(my_code)