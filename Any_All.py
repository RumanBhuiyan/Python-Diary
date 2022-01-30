# any(iterable) returns True if iterable has atleast one Truthy item
# all(iterable) returns True if all items are Truthy
numbers = [1,2,3,4,5]

print(any(numbers)) # True
print(all(numbers)) # True

keep = [ num for num in range(0,4,1)]

print(all([num for num in range(0,4,1)])) # False
print(any([num for num in range(0,4,1)])) # True

# any can be used to check if any of the list item satisfy a certain condition
realNumbers = [-2,-1,10]
print(any([ num for num in realNumbers if num>0])) # True

# all can be used to check if all of the list item satisfy a certain condition
realNumbers = [-2,-1,-10]
print(all([ num for num in realNumbers if num<0])) # True