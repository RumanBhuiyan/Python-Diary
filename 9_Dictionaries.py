# dictionary in python is simmillar as object in javascript
myDictionary = {
    'Ruman': 1,
    'Robiul': 2,
    'Shahadat': 3
}
# accessing keys,values,items of a dictionary
print(f'Dictionary keys: {list(myDictionary.keys())}')
print(f'Dictionary values: {list(myDictionary.values())}')
print(f'Dictionary items: {list(myDictionary.items())}')
# accessing individual item
print('First Item Value: ', str(myDictionary['Ruman']))
print('Second Item Value: ', str(myDictionary.get('Robiul')))
# changing value of any key
myDictionary['Shahadat'] = 43
print(myDictionary)
# adding new item to dictionary
myDictionary['parbez'] = 5
print(myDictionary)


def doSomething(name):
    print(f'Hello {name}')


# dictionary can contatin function too
another = {
    # assigning reference of doSomething function,not output after execution
    'something': doSomething
}
another['something']('Revenger076')  # calling function right now
