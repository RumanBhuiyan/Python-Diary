> ## 1. String Interpolation or Foramatting
```python
    a=2
    b=3

    print("Number ",a,b) # Number 2 3
    print("Number {1} {0}".format(a,b))# Number 3 2
    print(f'Number {a} {b}') # Number 2 3
```
> ## 2. Input 
```python
    a=int(input("Enter the first Number : "))# Renders the text Enter the first number but accepts string from command line
    b=int(input("Enter the second Number : ")) #  and make it int type then assign it

    print(f'Summation of two number is {a+b}')
```
> ### 3. Strings
```python
      myString = "Welcome to my Python tutorial"

      print('Length of the string is ', len(myString))
      print('Upper case : ', myString.upper())
      print('Lower case : ', myString.lower())
      print('Capitalize : ', myString.capitalize())
      print('Title : ', myString.title())
      
      # in & not in operator in python
      print('Is python exist in the string ? ', 'Python' in myString)
      print('Is java exist in the string ? ', 'Java' in myString)
      print('Doesn\'t java exist in the string ? ', 'Java' not in myString)

      print('Find Python at index : ', myString.find('Python'))
      print('Find & replace Python by Java: ', myString.replace('Python', 'Java'))

      print('Character at position 4: ', myString[3])
      print('Characters from beginning to end: ', myString[0:])
      print('Characters from beginning to 14 index: ', myString[0:14])
      print('Printing characters from backwards : ', myString[-2])
```
> ## 4. List
```python
      names = ['Ruman', 'Robiul', 'Shahadat', 'Ontor', 'Parbez']
      numbers = [5, 4, 10, 34, 2, 9, 1]

      print('names is ', type(names))
      print('How many length ? ', len(names))

      # accessing & change item in list
      print('First name: ', names[0])
      names[0] = 'Bhuiyan'
      print('First name: ', names[0])

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

```
> ## 5. Tuple
```python
      # tuple is simmillar as list but the difference is
      # tuple immutable & faster than list but pop(),remove()etc absent in tuple
      names_tuple = ('Ruman', 'Robiul', 'Ontor', 'Parbez', 'Shahadat')

      print("At the beginning: ", names_tuple)
      print('Second item: ', names_tuple[1])
      # its not valid ->names_tuple[1] = 'Sany' because tuple is immutable

      # adding items to tuple:
      names_tuple = names_tuple + ('sany',)
      print("After new item: ", names_tuple)
      print("converting to list: ", list(names_tuple))

      # tuple unpacking: == Destructuring in javascript
      nameList = [(1, 'Ruman'), (2, 'Robiul'), (3, 'Shahadat'), (4, 'Ontor')]
      for index, name in nameList:
          print(f'{index}: {name}')

      for eachName in nameList:
          print(f'{eachName[0]} : {eachName[1]}')

```
