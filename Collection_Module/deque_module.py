from collections import deque

# deque  stands for double ended queue
# in deque we can append in left,right
# delete from left and right thus deque adds spicy to list

# popleft, append operation takes O(1) time in Deque but O(n) in list
# so use deque instead of list 

numbers = deque()

numbers.append(1) # [1]
numbers.appendleft(2) #[2,1]
numbers.append(3) # [2,1,3]
numbers.appendleft(4) #[4,2,1,3]

print(numbers)

numbers.pop() #[4,2,1]
numbers.popleft() #[2,1]
print(numbers)

# right shift one place for each item
numbers.rotate(1)
print(numbers)

# left shift one place for each item
numbers.rotate(-1)
print(numbers)

# there are some other methods of deque check them in help(numbers)
