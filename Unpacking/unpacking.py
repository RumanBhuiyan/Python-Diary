# tuple unpacking 
def get_sum(*args):
    total = 0
    for num in args:
        total += num
    return total


numbers = (1,2,3,4,5)
print(get_sum(*numbers))
# this line is similar as print(get_sum(1,2,3,4,5))
# so we aren't passing whole tuple as an argument rather 
# unpacking its all values & passing them to function

# dictionary unpcaking
def print_values(**kwargs):
    for key,value in kwargs.items():
        print(f'key = {key} value = {value} ') 

my_dict = {'one':1,'two':2,'three':3}
print_values(**my_dict)
# this line is similar as print_values({'one':1,'two':2,'three':3})
# so we aren't passing whole dictionary as an argument rather 
# unpacking its all values & passing them to function