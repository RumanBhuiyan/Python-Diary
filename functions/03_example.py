def get_sum3(**kwargs):
    summation = 0
    for _, value in kwargs.items():
        summation += value
    return summation


# calling approach of example - 03 : 
# **kwargs receives arguments as dictionary and its arguments are optional
# kwargs is short of keyword arguments. you can call it whatever you want but ** before kwargs is must because you know why

print(get_sum3())
print(get_sum3(a = 1, b = 2, c = 3))