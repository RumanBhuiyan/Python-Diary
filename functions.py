# one function can take more than one argument
# args receive arguments as tuple
def get_sum(*args):
    print(type(args))
    sum = 0
    for number in args:
        sum +=number
    return sum

print("summation is ",get_sum(1,2,3))
print("summation is ",get_sum(1,2,3,4))

# function receiving argument as dictionary
# kwargs is used by default as a naming convention
def print_dic(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

print_dic(One="1",two="2",three=3)

# parameter ordering
# def functin_name (a,*args,name="ruman",**kwargs)
# when you will multiple arguments to a function then you should follow the order


def complete_function(name,*args,**kwargs):
    print(name)
    print(args) # args collects non-positional multiple arguments
    print(kwargs) # kwargs collects positional multiple arguments or dictionary

complete_function("Ruman",1,2,3,4,5,lname="Bhuiyan",age=23)