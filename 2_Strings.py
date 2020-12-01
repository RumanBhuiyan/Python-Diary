myString = "Welcome to my Python tutorial"

print('Length of the string is ', len(myString))
print('Upper case : ', myString.upper())
print('Lower case : ', myString.lower())
print('Capitalize : ', myString.capitalize())
print('Title : ', myString.title())

print('Is python exist in the string ? ', 'Python' in myString)
print('Is java exist in the string ? ', 'Java' in myString)
print('Doesn\'t java exist in the string ? ', 'Java' not in myString)

print('Find Python at index : ', myString.find('Python'))
print('Find & replace Python by Java: ', myString.replace('Python', 'Java'))

print('Character at position 4: ', myString[3])
print('Characters from beginning to end: ', myString[0:])
print('Characters from beginning to 14 index: ', myString[0:14])
print('Printing characters from backwards : ', myString[-2])
