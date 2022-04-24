def get_sum2(*args):
    summation = 0
    for number in args:
        summation += number
    return summation


# calling approach of example - 02 : 
# *args receives arguments as tuple and arguments are optional in this case
# args is short form of arguments. you can name it whatever you want but * before args is must because you know why

print(get_sum2())
print(get_sum2(1))
print(get_sum2(1,2,3))