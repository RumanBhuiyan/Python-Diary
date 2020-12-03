name = "Ruman"
data = '12345'

# if characters len not equal then extra character will gone
newDict = dict(zip(name, data))  # zip operation
print(newDict)
print(list(zip(*newDict)))  # unzip operation
