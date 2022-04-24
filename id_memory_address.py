"""
    id(variable_name) returns the memory address of that variable
"""

name = "Ruman"
reversed_name = name[::-1]

print(f'Memory address of name : {id(name)}')
print(f'Memory address of reversed_name : {id(reversed_name)}')