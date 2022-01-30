# article :  https://dev.to/v_it_aly/python-deque-vs-listwh-25i9
# deque is implemented on doubly linked list and list is on array
# thats why append and pop operations are fater in deque than list 
# append operation takes O(1) time in deque but O(n) in list
# but accessing element takes O(n) time in deques but O(1) in list
# when to use Deque and when to use list ?
# -- if your problem only cares about last or first item then deques is faster
# -- if your problem has to work with random access values then use list
import time 
from collections import deque

# create an odd numbers list
numbers_one = []

odd_start = time.time_ns()
for num in range(1,1000000):
    numbers_one.append(num)
odd_end = time.time_ns()

print(f"Append takes {odd_end - odd_start} nanoseconds in list")

# create an even numbers deque
numbers_two= deque()

even_start = time.time_ns()
for num in range(1,1000000):
    numbers_two.append(num)
even_end = time.time_ns()

print(f"Append takes {even_end - even_start} nanoseconds in Deque")

print(f"List took {((odd_end-odd_start)-(even_end-even_start))} nanoseconds more than Deque")

# output
# Append takes 73167500 nanoseconds in list
# Append takes 68944300 nanoseconds in Deque
# List took 4223200 nanoseconds more than Deque