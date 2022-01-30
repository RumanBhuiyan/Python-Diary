# raising our own error like TypeError , ValueError
keep = input('Enter any of among AEIOU : ')

if keep in 'AEIOU':
    print("Good job")
else :
    raise ValueError('Please enter correct value')

# handing errors using try except block
string = ''
try :
    keep  = int(input())
    result = keep /0
except:
    string = 'bad job'
    print('An error occured')
else :
    string = 'good job'
    print('Executed as except block is not executed')
finally:
    print(string)

