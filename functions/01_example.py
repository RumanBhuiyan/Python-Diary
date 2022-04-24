# example - 01 default value of a = 0, b = 0
def get_sum(a = 0, b = 0):
    return a + b


# different calling approach of example - 01 : a,b arguments are mandatory to pass
print(get_sum())
print(get_sum(100))
print(get_sum(1, 2))
print(get_sum(a = 1, b = 2))
print(get_sum(b = 3, a = 1))

# get_sum(1, 2) here 1,2 are called un-named arguments or positional arguments
# get_sum(a = 1, b = 2) here a = 1, b = 2 are called named arguments.
