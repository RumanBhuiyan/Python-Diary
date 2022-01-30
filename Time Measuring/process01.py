from time import time


def run_ntimes(n):
    for i in range(n):
        pass


start_time = time() # take current time in seconds
run_ntimes(100000000)
finish_time = time() #take current time in seconds
print(f'run_ntimes() function took {finish_time - start_time} seconds to execute')

# N.B :
# time module may also include time of background process except this python program
# probably that's why we get different time as output everytime when we run the program
# so for measuring exact time taken by the program, time module isn't perfect 
# for that purpose, we should use timeit module.because timeit module provides better result 
# than time module