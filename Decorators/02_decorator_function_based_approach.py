def GetName(func):
    # func hold the referece of passing function
    # Here, func = name or func = get_sum

    def wrapper_func(*args, **kwargs):
        print(f'From wrapper function of GetName function')
        print(func(*args, **kwargs))
    
    return wrapper_func

# proces - 01 :
@GetName
def name():
    return "Ruman Bhuiyan"

# name() calls wrapper_func(*args, **kwargs) of GetName function under the hood
name()


# process - 02:
@GetName
def get_sum(*args, **kwargs):
    summation = 0

    for number in args:
        summation + number

    for _, value in kwargs.items():
        summation += value
    
    return summation

# get_sum() calls wrapper_func(*args, **kwargs) of GetName function under the hood
get_sum(1, 2, 3, a = 5, b = 6 )
