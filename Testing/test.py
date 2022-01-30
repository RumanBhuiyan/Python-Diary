string = input()
new_string = ''

for character in list(string):
    if character.islower():
        new_string += character.upper()
    elif character.isupper():
        new_string += character.lower()
    else :
        new_string += character

print(new_string)