#deque provides O(1) time complexity for append and pop operations 
#as compared to list with O(n) time complexity.

from collections import deque

# declaring deque 
evenNumbers=deque(list())
oddNumbers=deque([])

#adding items right/end
evenNumbers.append(4)
evenNumbers.append(6)
oddNumbers.append(3)
oddNumbers.append(5)
print(f'Even numbers: {evenNumbers} oddNumbers : {oddNumbers}')

#adding items to left
evenNumbers.appendleft(2)
oddNumbers.appendleft(1)
print(f'Even numbers: {evenNumbers} oddNumbers : {oddNumbers}')

#removing items from right
keep=evenNumbers.pop() # poping item from end and storing into a variable
another=oddNumbers.pop()
print(f'Even numbers: {evenNumbers} oddNumbers : {oddNumbers}')

#removing items from left 
keep=evenNumbers.popleft() # poping item from left end storing into a variable
another=oddNumbers.popleft()
print(f'Even numbers: {evenNumbers} oddNumbers : {oddNumbers}')

#counting elements in deque
numbers=deque([1,2,2,3,3,3,4,4,5])
print(f'How many times 4 ? : {numbers.count(4)}')

# iterating 
for i in range(len(numbers)):
    print(numbers[i],end=' ')

#clearing a deque 
numbers.clear()
print(f'\n Now numbers deque is {numbers}')

