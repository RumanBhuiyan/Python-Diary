# article resource : 
# https://www.guru99.com/timeit-python-examples.html
# https://www.askpython.com/python-modules/python-timeit-module
# https://www.geeksforgeeks.org/timeit-python-examples/

# timeit.timeit(setup,stmt,timer,number) takes 4 arguments
# setup -> wrap your import statements inside '' like 'import random' and assign it to a
#           variable.pass setup=variable_name. python will execute this before running stmt
# stmt ->  wrap your code blocks inside ''' ''' & assign into a variable. then pass the 
#           variable to stmt like stmt = variable_name.python will run this code.
# time -> you can ignore this. because its default value is Timer object assigned by python 
#           itself.
# number -> its default value is 1000000(1 million) or you can specify number here.
#           this number tells python how many times python shoul execute your code in stmt
# timeit.repeat() -> provides an extra argument repeat where you can mention how many times
#           pyton should repeat like repeat=3.

from timeit import timeit
my_setup = "from cmath import sqrt"

my_stmt = '''
def get_sqrts():
    number_roots = []
    for i in range(1,100):
        number_roots.append(sqrt(i))
'''

print(f'{timeit(setup=my_setup,stmt=my_stmt,number=10000000)} seconds')


# evaluating time of single statement
print(f'{timeit(setup=my_setup,stmt="x=sqrt(5)",number=100000)} seconds')