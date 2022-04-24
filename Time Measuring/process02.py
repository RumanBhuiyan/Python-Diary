import timeit


def run_ntimes(n):
    for i in range(n):
        pass


start_time = timeit.default_timer() # take current time in seconds
run_ntimes(100000000)
finish_time = timeit.default_timer() #take current time in seconds
print(f'run_ntimes() function took {finish_time - start_time} seconds to execute')

# N.B :
# timeit module also shows different times everytime when we run the program but these
# times are nearer to each other and less than those times taken by process01.py.
# so we can use it because it's more convenient than process01.py