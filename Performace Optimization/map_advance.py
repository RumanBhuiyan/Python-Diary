# Problem-01 : making upper all character of  a list

# Solution - 01  :
characters = ['a','b','c','d']

for index,c in enumerate(characters):
    characters[index] = c.upper()

print(characters)

# Solution - 02 :
character_set = ['a','b','c','d']
character_set = list(map(str.upper,character_set))
print(character_set)

# output
# ['A', 'B', 'C', 'D']
# ['A', 'B', 'C', 'D']
# second approach increase the readablity of code and makes code shorte