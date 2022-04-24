# this type of queue can be used for shared resources
from queue import LifoQueue


numbers = LifoQueue()

# adding items
numbers.put(1)
numbers.put(2)
numbers.put(3)

while numbers:
    if numbers.empty():
        break
    print(numbers.get())