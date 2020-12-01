names = ['Ruman', 'Robiul', 'Shahadat', 'Ontor', 'Parbez']
numbers = [5, 4, 10, 34, 2, 9, 1]

print('names is ', type(names))
print('How many length ? ', len(names))

print('Minimum number of the list: ', min(numbers))
print('Maximum number of the list: ', max(numbers))
print('Summation of numbers in the list: ', sum(numbers))
numbers.sort()  # sorting list in ascending order
print('Sorted List : ', numbers)
numbers.sort(reverse=True)  # sorting list in descending order
print('Reversely Sorted List: ', numbers)

# inseting item into list
numbers.append(100)  # adding item to end
numbers.insert(6, 12)  # adding item at certain index
print('After adding new item number list : ', numbers)
numbers.remove(100)
print('After removing a item number list : ', numbers)
keep = numbers.pop()  # extracting last item and storing in a variable
anotherKeep = numbers.pop(-1)
print('Poping tems are ', keep, ' ', anotherKeep)
print('After poping a item number list : ', numbers)

# adding two list
numbers.extend(names)
print('Combining two list : ', numbers)
print('Copy of new list: ', names.copy())
print('Copy of new list: ', list(names))
#split & join
# seperate items where finds ,
print('Spliting list : ', str(names).split(','))
print('Second time spliting : ', "-".join(str(names)).split(','))
# deleting or clearing list
names.clear()
del numbers
