# bisect module helps us to get the index of a value in sorted ordered iterable where we can insert that value
from bisect import bisect, bisect_left, bisect_right

numbers = [1, 2, 3, 3, 4, 5]

# bisect_left(iterable,value) => returns the left most possible index for inserting the value
# bisect_right(iterable,value) => returns the right most possible index for inserting the value
# bisect(iterable,value) => same as bisect_right

print(bisect_left(numbers,3))
print(bisect(numbers,3))
print(bisect_right(numbers,3))

print(f'Numbers before adding new item : {numbers}')
numbers.insert(bisect(numbers,6),6)
print(f'Numbers after adding new item : {numbers}')