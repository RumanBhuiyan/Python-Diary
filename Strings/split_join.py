# split seperates items based on a character passed into split()
numbers = '1 2 3 4 5 6 7'
numbers = numbers.split(' ') # split basis on whitespace
print(numbers) # ['1', '2', '3', '4', '5', '6', '7']

# join basically combine all list items putting character of ''.join()
# between every two elments
keep = '123 45 678'
keep = keep.split(' ')
print('-'.join(keep)) # 123-45-678

# to check which builtin functions can be used upon any variable use dir() like below
print(dir(keep))
