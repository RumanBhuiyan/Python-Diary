"""
    var_
    function_name_
    variable,function name with _ in end are used to avoid confliction with python inbuilt resources.
    If you provide a name to a variable or a function that conflicts or may conflict with python keywords.
    built in functions then you can solve this issue just adding a single _ in end of your given name.
"""

def print_(name):
    print(f'So you are {name}')

print_("Ruman")