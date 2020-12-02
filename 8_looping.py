# while loop
i = 1
while i < 6:
    print(i, end=" ")  # end of i don't print a newline rather print space
    i += 1
# for-loop
# type-1
print()  # printing a newline
for i in 'Ruman':
    print(i, end=" ")
# type-2
print()
for item in ['Ruman', 'Robiul', 'Ontor', 'Shahadat']:
    print(item, end=" ")
# type-3
print()
for i in range(5):
    print(i, end=" ")
# type-4
print()
for i in range(2, 5):  # starts from 2 & end before 5
    print(i, end=" ")
# type-5
print()
for i in range(2, 20, 4):  # starts from 2,increse by 4 and stop before 20
    print(i, end=" ")

# enumeration
print('\nEnumeration: ')
# second parameter says begin from where
for index, name in enumerate(['Ruman', 'Robiul', 'Shahadat'], 1):
    print(index, name)
