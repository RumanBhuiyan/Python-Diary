"""
    setdefault(key,value)
    this insert new key in the dictionary with the provided value and returns value of that key
    if the key already exists then setdefault() returns that key value and doesn't update the value
"""

numbers = {
    "One" : 1,
    "Two" :2,
    "Three" : 3,
}

# scenario - 01
print(numbers.setdefault("Four", 4))
print(numbers)

# scenario - 02
print(numbers.setdefault("One",100))
print(numbers)