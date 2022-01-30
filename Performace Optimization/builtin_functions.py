# in python you can use built in sum instead of your own sum implementation
# thus built in functions can reduce time of your program but not always
# sum, max, any , map are built on c so use them to get better optimization
import time

def get_summation_builtin(numbers):
    return sum(numbers)

def get_summation(numbers):
    summation  = 0
    for num in numbers:
        summation += num 
    return summation

# lets create a large list to visually detect time difference
numbers = list(range(1000000))

t1 = time.time_ns()
result = get_summation_builtin(numbers)
t2 = time.time_ns()
print(f"Built in summation takes {t2 - t1} nanoseconds")

t3 = time.time_ns()
result = get_summation(numbers)
t4 = time.time_ns()
print(f"Own implementation summation takes {t4 - t3} nanoseconds")

# output
# Built in summation takes 16569600 nanoseconds
# Own implementation summation takes 28062200 nanoseconds