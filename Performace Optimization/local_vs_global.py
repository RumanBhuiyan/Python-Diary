# use local functions and variables instead of global variables & functions
# because local variables and functions are faster than global variables & functions
import time 

t1 = time.time_ns()
for _ in range(100000):
    pass
t2 = time.time_ns()

print(f"global scope takes {t2 - t1} nanoseconds")

def print_nothing():
    t1 = time.time_ns()
    for _ in range(100000):
        pass
    t2 = time.time_ns()
    return t2,t1

t4,t3 =print_nothing()
print(f"local scope takes {t4 - t3} nanoseconds")

# output
# global scope takes 1999300 nanoseconds
# local scope takes 1000800 nanoseconds