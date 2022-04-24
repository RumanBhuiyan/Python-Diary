
# scenario - 01 : (_ prfixed variables, functions are for this file internal use )
_age = 24
def _get_age():
    return _age

# below methods become available 
def get_name():
    return "Ruman"

def your_age():
    return _get_age()