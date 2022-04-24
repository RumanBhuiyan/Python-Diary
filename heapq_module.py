# heap concept clear tutorial : https://www.youtube.com/watch?v=8noP3YjjJCM

from heapq import heapify, heappush, heappop, heapreplace, nlargest, nsmallest

numbers = [1, 4, 10, 2, 7, 6]

# heapify(iterable) creates the min heap tree 
heapify(numbers)
print(f'numbers after heapify(): {numbers}')

# heappush(iterable,value) add new item in end of heap tree then heapify() all items by itself
heappush(numbers, -1)
print(f'numbers after heappush(): {numbers}')

# heappop(iterable)removes the smallest item from heap tree then heapify() all items by itself
heappop(numbers)
print(f'numbers after heappop(): {numbers}')

# heapreplace(iterable, value) replace the smallest item by this value and heapify() itself
heapreplace(numbers,-5)
print(f'numbers after heapreplace(): {numbers}')

print(f'3 largest values of heap : {nlargest(3,numbers)}')
print(f'3 smallest values of heap : {nsmallest(3,numbers)}')