def verify_and_append(keep, values):
    if len(keep):
        values.append(keep)
        keep = ''
    return keep
    

def my_split(sentence):
    splitted_values = []
    temp = ''
    for character in sentence:
        if  character.isspace():
            temp = verify_and_append(temp, splitted_values)
        else:
            temp += character
    verify_and_append(temp, splitted_values)
    
    return splitted_values



print(my_split('1 2 3'))
print(my_split('1 2 3  '))
print(my_split('  1 2 3'))
print(my_split('1    2 3'))
print(my_split('    1    2   3 '))
print(my_split('123   '))
print(my_split('   123   12 136   '))
    