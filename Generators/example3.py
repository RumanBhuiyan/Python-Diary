# example - 03
def my_range2(start, stop, step = 1):
    start -= step
    while start + step < stop:
        start += step
        yield start

for num in my_range2(20, 100, 10):
    print(num)