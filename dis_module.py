"""
    dis module helps us to visualize byte code/machine code which machine produces at the time of 
    execution 
"""

from dis import dis

def greet(name):
    return f'Hi {name}'

dis(greet)

#   4           0 LOAD_CONST               1 ('Hi ')
#               2 LOAD_FAST                0 (name) 
#               4 FORMAT_VALUE             0
#               6 BUILD_STRING             2
#               8 RETURN_VALUE