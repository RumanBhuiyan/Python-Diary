def get_sum4(a = 0, b = 0, *args, **kwarg):
    summation = a + b

    for number in args:
        summation += number
    
    for _, value in kwarg.items():
        summation += value
    
    return summation


# calling approach of example - 04
print(get_sum4())
print(get_sum4(1))
print(get_sum4(1, 2))
print(get_sum4(1, 2, 3, 4, c =25))
print(get_sum4(1, 2, 3, 4, c = 5, d = 6))


# parameter ordering that must be followed
# def function_name (positional arguments, *args, **kwargs)