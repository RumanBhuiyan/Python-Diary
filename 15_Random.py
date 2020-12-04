import random

print(random.randint(1, 10))  # select a random number within 1 & 10
print(random.randrange(1, 10, 2))  # select a number from [1 3 5 7 9]

names = ['Ruman', 'Robiul', 'Ontor', 'Shahadat', 'Parbez']
print(random.choices(names))  # select a random item from names
print(random.sample(names, 3))  # select any 3 items from names
random.shuffle(names)  # change the order of list
print(names)

# getting help to know details about a pre-built function
help(random.shuffle)
