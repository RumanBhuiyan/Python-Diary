# https://docs.python.org/3/library/array.html
from array import array

# c like array in python. here we are telling python to store only integer
numbers = array('i',[1,2])
numbers.append(4)
numbers.append(5)

for num in numbers:
    print(num,end=' ')