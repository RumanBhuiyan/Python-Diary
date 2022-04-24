"""
    deque  stands for double ended queue
    in deque we can append in left,right
    delete from left and right thus deque adds spicy to list

    popleft, append operation takes O(1) time in Deque but O(n) in list
    so use deque instead of list 

    As Deque is implemented on doubly linked list thats why append,pop operation from both end and front
    takes O(1) time complexity but random access of element takes O(n) time whereas append operation takes
    O(n) time in list but O(1) time in random access of element . So you can use deque as stack,queue
"""
from collections import deque


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

# we can mention the length of a deque like deque(iterable,maxlen=10)
# that's why if overflow happens due to append() operation then leftmost/first element is deleted
# otherwise if overflow occurs due to appendLeft() operation the rightmost/last element is deleted
