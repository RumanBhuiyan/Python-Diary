import secrets


print(f'{secrets.randbelow(10)}') # select a number within 0-10 excluding 10
print(f'{secrets.randbits(4)}') # choose 4 random binary bits like 1011 ,0101


vowels = ['A','E','I','O','U']
print(f'{secrets.choice(vowels)}')# pick a random item from an iterable