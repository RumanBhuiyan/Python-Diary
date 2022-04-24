import random  # best practise says that import the only thing that you want

print(f'Random Number within 0-1 : {random.random()}')
print(f'Random Floating Number within 0-1 : {random.uniform(1,10)}')
print(f'Random Int Number within 1-10 including 10 : {random.randint(1,10)}')
print(f'Random Int Number within 1-10 excluding 10 : {random.randrange(1,10)}')

vowels = ['A','E','I','O','U']
print(f'Random Choice : {random.choice(vowels)}')
print(f'Random Choices : {random.choices(vowels,k=2)}')
print(f'Random Sample : {random.sample(vowels,2)}')


# shuflling an iterable
random.shuffle(vowels)
print(f'Vowels after shuffling : {vowels}')


#getting repeatitive value in random setting the seed
random.seed(1)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())