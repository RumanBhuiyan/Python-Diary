class GetName:
    def __init__(self,func):
        # hold the reference of passing function
        # Here self.func = name or self.func = get_sum
        self.func = func
    

    # __call__(self) is such a dunder method which makes our class instance callable
    # so lets take this advantage to create a decorator using class based approach
    # N.B => passed functions arguments are received by __call__(*args, **kwargs)
    def __call__(self, *args, **kwargs):
        print(f'From __call__ ....')
        print(self.func(*args, **kwargs))

# proces - 01 :
@GetName
def name():
    return "Ruman Bhuiyan"

# name() invokes __call__(self) of GetName class under the hood
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

# get_sum() invokes __call__() of GetName class under the hood
get_sum(1,2,3, a = 5, b = 6 )
