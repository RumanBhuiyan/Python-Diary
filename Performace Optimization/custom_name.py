import time 

numbers = []
t1 = time.time_ns()
for num in range(100000):
    numbers.append(num)
t2 = time.time_ns()
print(f"Direct function took {t2 - t1} nanoseconds")

another_list = []
# as we are storing the reference of append function of list into add_number
# python wont take re-evaluation time in below code at the time of adding item 
add_number = another_list.append

t3 = time.time_ns()
for num in range(100000):
    add_number(num)
t4 = time.time_ns()
print(f"Custom function took {t4 - t3} nanoseconds")

# output : 
# Direct function took 6136400 nanoseconds
# Custom function took 6081500 nanoseconds