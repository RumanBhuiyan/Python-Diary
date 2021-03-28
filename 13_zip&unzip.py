name = "Ruman"
data = '12345'

# if characters len not equal then extra character will gone

newDict = dict(zip(name, data))
print(newDict)  # {'R': '1', 'u': '2', 'm': '3', 'a': '4', 'n': '5'}
print(list(zip(*newDict)))  # unzip operation
#[('R', 'u', 'm', 'a', 'n')]
