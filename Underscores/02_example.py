""" _variable 
    _function
    these types are used to denote that the variable or function is for internal use.
    But if you import like, from <module_name> import * then variables,functions named with
    prefix _ wont be imported in that file.

    In my words. _var,_function are protected variable and function
"""

# use case - 01 (wildcard * importing can't access _ prfixed variables and functions)
from helper_methods import *

# print(_age) # throws error
# _get_age() # throws error
print(get_name())

# use case - 02 (importing using as operator can accessed variables, functions prfixed with _)
import helper_methods as methods

print(methods._age)
print(methods._get_age())
print(methods.get_name())
