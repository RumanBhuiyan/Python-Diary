# raw_input() is used in pytho2 for taking user input instead of input() in python3
name = raw_input('Enter your name : ')
age = input('Age : ')

print('Hello {0}. You are {1} years old'.format(name,age))

# N.B though raw_input(),input() both are available in python2 but most people
# use raw_input() in python2 and input() because it has security issue