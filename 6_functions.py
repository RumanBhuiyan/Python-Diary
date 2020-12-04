# def= define function. one indentation= one tab
# age=22 is default value,if age value isn't sent as argument then it' printed
def printBio(name, age=22):
    print(f'name is {name}')
    print(f'age is {age}')

# function with return statement


def square(num):
    return num**2

# a function that can return so many things


def returnMany(num):
    return num*2, num*3, num*4


# inside main body lets call the function
# calling function without named parameter
printBio(input('Enter your name: '))
# lets call function with named parameter
keepName = input('Enter your friend name: ')
keepAge = int(input('Enter age: '))
printBio(name=keepName, age=keepAge)

# calling function who has return statement
print("Square of a number: ", square(num=int(input('Enter the number: '))))
# calling function who can return many things
print("double triple 4 times: ", returnMany(
    num=int(input('Enter the number: '))))

# passing to much arguments in a function


def printWhatever(*args):
    print(args)


printWhatever(1, 2, 3, 4, 5, 6, 7)
# passing a dictionary to function


def keepDictionary(**mydict):
    for key in mydict.keys():
        print(f'{key}: {mydict[key]}')


keepDictionary(a=1, b=3, c=3)
# another way


def keepDictionary(**mydict):
    for item in mydict.items():
        print(f'{item[0]}: {item[1]}')


keepDictionary(a=1, b=3, c=3)
