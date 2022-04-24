"""
    for catching error and displaying error message in our customized way we can use 
    exc_info function from sys module like below
"""

from sys import exc_info


try:
    resutl  = 5 /0
except:
    print(f'Error : {exc_info()[0]} {exc_info()[1]}')