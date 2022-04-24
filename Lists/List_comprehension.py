""" list is implemented on dynamic array """

# list comprehension without condition
# convert space-separated integers to list
numbers = '1 2 3 4 5 6'
numbers = [int(num) for num in numbers.split()]
print(numbers) # [1, 2, 3, 4, 5, 6]

# list comprehension with if logic
natural = '1 2 3 4 5 6'
natural = [ int(num) for num in natural if num.isdigit() ]
print(natural) # [1, 2, 3, 4, 5, 6]

# list comprehension with if-else 
EvenOdds = '1 2 3 4 5 6'
EvenOdds = [ 'Even' if num%2==0 else 'Odd' for num in natural]
print(EvenOdds) # ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

# Nested List comprehension
keep = [ i*j  for i in range(1,3) for j in range(1,11)]
print(keep)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# how its working under the hood.
# keep = []

# for i in range(1,3):
#     for j in range(1,11):
#         keep.append(f'{i}*{j} = {i*j}')

# print(keep)

# structure of list comprehension
# variable = [body_statement loop_statement]
# varibale = [body_statement first_loop nested_loope]

# knowing all the built in methods of list
# help(list)