# set is a collection of un-ordered unique items
numbers = {1,2,2,2,3}
print(numbers) # {1, 2, 3}

# adding item
numbers.add(4)
numbers.add(5)

# remove item
numbers.remove(5)
numbers.discard(6) # discard wont show error if item doesn't exist

# copying set
another = numbers.copy()

# deleting whole set
another.clear()

# as set items aren't ordered so you can't access them by index like numbers[0]
# for accessing item 
for num in numbers:
    print(num)

# mathematical set union & intersection operation
print(numbers.union({4}))
print(numbers.intersection({2}))

# set comprehension
squares = { x**2  for x in range(0,10)}
print(squares) # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# few other set methods
setA = {1,2,3,4,5,10,11,12}
setB = {1,2,3}
setc = {7,8,9}

print(f'Differeneces between SetA and SetB : {setA.difference(setB)}')
# setA.difference_update(setB) # find difference and assign result to setA

# symmetric difference = A - B in language of set
print(f'Symmetric Differeneces between SetA and SetB : {setA.symmetric_difference(setB)}')
print(f'Symmetric Differeneces between SetA and SetB : {setA -setB}')
# setA.symmetric_difference_update(setB) # find symmetric difference and assign result to setA

print(f'Intersection between SetA and SetB : {setA.intersection(setB)}')
# setA.intersection_update(setB) # find intersection and assign result to setA

print(f'Is SetA subset of SetB ? : {setA.issubset(setB)}')
print(f'Is SetA superset of SetB ? : {setA.issuperset(setB)}')
print(f'SetA & SetB dijoint ? : {setA.isdisjoint(setc)}')# disjoint -> there is no intersection
