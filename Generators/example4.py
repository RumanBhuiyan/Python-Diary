# example - 04 
def my_range3(*args):
    start, stop, step = 0, 0, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args[0:2]
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise Exception('Expected 1-3 arguments')
    
    start -= step
    while start + step < stop:
        start += step
        yield start
    

for num in my_range3(1,5,2):
    print(num)