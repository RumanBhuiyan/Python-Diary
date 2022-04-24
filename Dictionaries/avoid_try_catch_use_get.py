numbers = {
    "One" : 1,
     "Two" :2,
}

# get method of dictionary returns None if key doesn't exist in dictionary
print(numbers.get('Three'))

# we can also tell python what to return if it doesn't find the key like below
print(numbers.get('Three', -1))