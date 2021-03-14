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
    a=int(input("Enter the first Number : "))
    b=int(input("Enter the second Number : ")) 

    print(f'Summation of two number is {a+b}')
    
    #taking space seperated inputs in python
    #process : 01 using list comprehension
    
    numbers = input("Enter the numbers : ")
    numbers=numbers.split() # seperating words/strings basis on space
    numbers = [int (x) for x in numbers] # converting each string to int
    print(numbers)

    #process : 02  using map function 
    # map(function,list) output the modified list performing function on each item of the list
    
    numbers=list(map(lambda x : int(x),input("Enter numbers : ").split()))
    print(numbers)

    #process : 03 using int() prebuilt function as parameter of map
    
    numbers =list(map(int,input("Enter numbers : ").split()))
    print(numbers)
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
> ## 6. Set
```python
        # Set is simmillar as Mathematical set we read in mathematics
        # sorted(list/tuple/set) ,reversed(list/tuple) pre-built functions
        my_friends = {'a', 'b', 'c', 'd', 'e'}
        his_friends = {'c', 'd', 'f', 'g', 'h'}
        # union operation
        print("All friends : ", sorted(my_friends.union(his_friends)))
        print("All friends another way : ", my_friends | his_friends)
        # intersection operation
        print("Common Friends: ", my_friends.intersection(his_friends))
        print("Common Friends: ", my_friends & his_friends)
        # difference operation
        print("They aren't my friends: ", his_friends.difference(my_friends))
        print("They aren't my friends: ", his_friends - my_friends)

```
> ## 7. Dictionary
```python
        # dictionary in python is simmillar as object in javascript
        myDictionary = {
            'Ruman': 1,
            'Robiul': 2,
            'Shahadat': 3
        }
        # accessing keys,values,items of a dictionary
        print(f'Dictionary keys: {list(myDictionary.keys())}')
        print(f'Dictionary values: {list(myDictionary.values())}')
        print(f'Dictionary items: {list(myDictionary.items())}')
        # accessing individual item
        print('First Item Value: ', str(myDictionary['Ruman']))
        print('Second Item Value: ', str(myDictionary.get('Robiul')))
        # changing value of any key
        myDictionary['Shahadat'] = 43
        print(myDictionary)
        # adding new item to dictionary
        myDictionary['parbez'] = 5
        print(myDictionary)


        def doSomething(name):
            print(f'Hello {name}')


        # dictionary can contatin function too
        another = {
            # assigning reference of doSomething function,not output after execution
            'something': doSomething
        }
        another['something']('Revenger076')  # calling function right now

```
> ## 8. Function
```python
        # def= define function. one indentation= one tab
        # age=22 is default value,if age value isn't sent as argument then it' printed
        def printBio(name, age=22):
            print(f'name is {name}')
            print(f'age is {age}')

        # function with return statement
        def square(num):
            return num**2

        # a function that can return so many things
        def returnMany(num):
            return num*2, num*3, num*4

        # passing to much arguments in a function
        def printWhatever(*args):
            print(args)


        printWhatever(1, 2, 3, 4, 5, 6, 7)
        
        # passing a dictionary to function
        def keepDictionary(**mydict):
            for key in mydict.keys():
                print(f'{key}: {mydict[key]}')


        keepDictionary(a=1, b=3, c=3)
        
        # another way
        def keepDictionary(**mydict):
            for item in mydict.items():
                print(f'{item[0]}: {item[1]}')
```
> ## 9. Conditional Statements 
```python
        # if-elif-else block
        if operator in ['+', '-', '*', '/', '%']:
            if(operator == '+'):
                print(f"Summation is {num1+num2}")
            elif(operator == '-'):
                print(f"Subtraction is {num1-num2}")
            elif(operator == '*'):
                print(f"Product is {num1*num2}")
            elif(operator == '/'):
                print(f"division is {num1/num2}")
            else:
                print(f'Remainder is {num1%num2}')
        else:
            print('Enter the correct operator please!!')

        # ternay operator
        print('num1 is', 'Positive' if num1 >= 0 else 'Negative')
```
> ## 10. Looping 
```python
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

        # list comprehension nested loop
        numbers = [[x*y for x in range(1, 11)]for y in range(1, 11)]

        print(numbers)
        print(f'length is {len(numbers)}')
```
> ## 11. Try Catch Block
```python
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number : '))

        try:
            global result  # declaring global variable result
            result = num1 / num2
        except:
            result = 0
            print('Invalid input')
        finally:
            print(f'Quotient is ', result)
```
> ## 12. Class & Object
```python
        # to keep class body empty use the keyword 'pass'
        class Biodata:
            age = 24
            # constructor, here self is reference to Biodata class like as 'this'
            # you can use any word instead of self here

            def __init__(self, name, occupation):
                self.name = name
                self.occupation = occupation
            # string representation of the class,self bind this method to object

            def __str__(self):
                return f'{self.name} is a {self.occupation}'
            # build your own function to return anything's length
            # thus you can build your ownkeyword to perform a task

            def __len__(self):
                return len(self.name)

            def showBiodata(self):
                print('Name : ', self.name, ' Occupation : ', self.occupation)


        person = Biodata('Ruman', 'Engineer')
        print('Person\'s age: ', person.age)
        person.showBiodata()
        print(f'String representation of the class is {str(person)}')
        print(f'name\'s length: {len(person)}')
```
> ## 13. Inheritance
```python
        # python supports multi-class-inheritance
        class Bird:
            def fly(self):
                print('It can fly')


        # class Hen(Bird):  # inheriting Bird class
        # calling parent class constructor : Bird.__init__() or super().__init__()
        #     pass
        class Hen:
            def swim(self):
                print('It can swim')


        class Duck(Bird, Hen):
            pass

        print('Duck : ')
        newDuck = Duck()
        newDuck.fly()
        newDuck.swim()
```
> ## 14. Zip & Unzip 
```python
        name = "Ruman"
        data = '12345'

        # if characters len not equal then extra character will gone

        newDict = dict(zip(name, data))
        print(newDict)  # {'R': '1', 'u': '2', 'm': '3', 'a': '4', 'n': '5'}
        print(list(zip(*newDict)))  # unzip operation
        #[('R', 'u', 'm', 'a', 'n')]
```
> ## 15. Lambda Function
```python
        # lambda function
        def square(x): return x*x
        def cube(x): return x*x*x


        print(f'Square of 2: {square(2)}')
        print(f'Cube of 2 : {cube(2)}')
      
        def myfunc(num):
            return num % 2 == 0
            
        # list comprehension in single loop
        numbers = [num for num in range(1, 6)]
        doubles = [num*2 for num in numbers]
        evenNumbers = filter(myfunc, numbers)
        # filter return those item which evaluation is true,if x true return it
        oddNumbers = filter(lambda x: x % 2, numbers)

        print(f'Double numbers: {doubles}')
        print(f'Even numbers: {list(evenNumbers)}')
        print(f'Odd numbers: {list(oddNumbers)}')
```
> ## 16. Random Number 
```python
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
```
> ## 17. Map & filter 
```python
        # map , filter functions
        numbers = [1, 2, 3, 4, 5]

        def square(num):
            return num**2

        # using map function with named function
        squareNumbers = list(map(square, numbers))
        print(f'Square of Numbers : {squareNumbers}')
        # using map function with anonymous or lambda function
        cubeNumbers = list(map((lambda num: num**3), numbers))
        print(f'Cube of numbers: {cubeNumbers}')

        def even(num):
            return num % 2 == 0

        # using filter function with named function
        evenNumbers = list(filter(even, numbers))
        print(f'Even Numbers: {evenNumbers}')
        # using filter function with anonymous of lambda function
        oddNumbers = list(filter(lambda num: num % 2, numbers))
        print(f'Odd Numbers: {oddNumbers}')

        # map function returns items performing operation on each but
        # filter function return those item which satisfy the condition
```
> ## 18. Generators
```python
        import sys
        # whenever a function get yield keyword it allocates 112 bytes of memory
        # in memory  and stores value of local variable there.At the time of
        # each iteration it calculates i**2 and return it & forgets previous i value

        def sendGenerator(n):
            for i in range(1, n):
                yield i**2

        # if you call sendGenerator(100000000)it will also take 112 bytes of memory
        keep = sendGenerator(5)
        print(sys.getsizeof(keep), ' bytes')
        # you can't iterate over a generator more than once
        # each iteration, loop sasy keep send me your next number like next(keep)
        for num in keep:
            print(num, end=' ')
        # now keep is empty thats why below line will generate empty list
        print(f'\n{list(keep)}')

        # creating generator in another way
        numbers = (x**2 for x in range(1, 5))
        print(type(numbers))

        # iteration in another way
        myIteration = iter(numbers)
        print(next(myIteration), end=' ')
        print(next(myIteration), end=' ')
        print(next(myIteration), end=' ')
        print(next(myIteration), end=' ')
```
> ## 19. Date Time
```python
        import datetime

        print(datetime.date.today())
        print(datetime.date.today().day)
        print(datetime.date.today().month)
        print(datetime.date.today().year)
```
> ## 20. Regual Expression (RegEx)
```python
        # 1.https://www.programiz.com/python-programming/regex (Its great)
        # 2. https://www.w3schools.com/python/python_regex.asp
        # importing Regular expression
        import re

        txt = "The rain in Spain"
        # Find all lower case characters alphabetically between "a" and "m":
        x = re.findall("[a-m]", txt)
        print(x)

        txt = "That will be 59 dollars"
        # Find all digit characters:
        x = re.findall("\d", txt)
        print(x)

        txt = "hello world"
        # Search for a sequence that starts with "he", followed by
        # two (any) characters, and an "o":
        x = re.findall("he..o", txt)
        print(x)

        txt = "hello world"
        # Check if the whole string starts with 'hello':
        x = re.findall("^hello", txt)
        # another way: x = re.findall("\AThe", txt)
        print(f"Does the string start with hello ? {bool(x)}")

        txt = "hello world"
        # Check if the whole string ends with 'world':
        x = re.findall("world$", txt)
        print(f"Does the string ends with world ? {bool(x)}")

        txt = "The rain in Spain falls mainly in the plain!"
        # Check if the string contains "ai" followed by 0 or more
        # "n" characters:
        x = re.findall("ain*", txt)
        print(x)
        # Check if the string contains "ai" followed by 0 or more
        # "x" characters:
        x = re.findall("aix*", txt)
        print(x)

        txt = "The rain in Spain falls mainly in the plain!"
        # Check if the string contains "ai" followed by 1 or more
        # "n" characters:
        x = re.findall("ain+", txt)
        print(x)
        # Check if the string contains "ai" followed by 1 or more
        # "x" characters:
        x = re.findall("aix+", txt)
        print(x)

        txt = "The rain in Spain falls mainly in the plain!"
        # Check if the string contains "a" followed by exactly two "l" characters:
        x = re.findall("al{2}", txt)
        print(x)

        txt = "The rain in Spain falls mainly in the plain!"
        # Check if the string contains either "falls" or "stays":
        x = re.findall("falls|stays", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if "ain" is present at the beginning of a WORD:
        x = re.findall(r"\bain", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if "ain" is present at the end of a WORD:
        x = re.findall(r"ain\b", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string contains any digits (numbers from 0-9):
        x = re.findall("\d", txt)
        print(x)

        txt = "The rain in Spain"
        # Return a match at every no-digit character:
        x = re.findall("\D", txt)
        print(x)

        txt = "The rain in Spain"
        # Return a match at every white-space character:
        x = re.findall("\s", txt)
        print(x)

        txt = "The rain in Spain"
        # Return a match at every NON white-space character:
        x = re.findall("\S", txt)
        print(x)

        txt = "The rain in Spain"
        # Return a match at every word character 
        #(characters from a to Z, digits from 0-9, and the underscore _ character):
        x = re.findall("\w", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string ends with "Spain":
        x = re.findall("Spain\Z", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string has any a, r, or n characters:
        x = re.findall("[arn]", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string has any characters between a and n:
        x = re.findall("[a-n]", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string has other characters than a, r, or n:
        x = re.findall("[^arn]", txt)
        print(x)

        txt = "The rain in Spain"
        # Check if the string has any 0, 1, 2, or 3 digits:
        x = re.findall("[0123]", txt)
        print(x)

        txt = "8 times before 11:45 AM"
        # Check if the string has any digits:
        x = re.findall("[0-9]", txt)
        print(x)

        txt = "8 times before 11:45 AM"
        # Check if the string has any two-digit numbers, from 00 to 59:
        x = re.findall("[0-5][0-9]", txt)
        print(x)

        txt = "8 times before 11:45 AM"
        # Check if the string has any characters from a to z lower case,
        # and A to Z upper case:
        x = re.findall("[a-zA-Z]", txt)
        print(x)

        txt = "8 times before 11:45 AM"
        # Check if the string has any + characters:
        x = re.findall("[+]", txt)
        print(x)

        line = "My name is Ruman"
        # find the string Starts with R then any characters at any times then n
        x = re.findall("[R].+[n]", line)
        print(x)
```
> ## 21. Numbers Methods
```python
        # printing hexadecimal value of decimal number
        print(f"Hexa-decimal value of 24: {hex(24)}")
        # printing binary value of decimal number
        print(f"Binary value of 24: {bin(24)}")
        # printing absolute vaule of a decimal number
        print(f"Absolute value of -24: {abs(-24)}")
        # printing round vaule of a decimal number
        print(f"Round value of 24.567: {round(24.567)}")
        # printing x to the power y vaule of a decimal number
        print(f"2 to the 3 equals : {2**3}")
        print(f"2 to the 3 equals : {pow(2,3)}")
        # printing a to the power b mod c
        print(f'16**12 mod 11 equals to {16**12 % 11}')
        print(f'16**12 mod 11 equals to {pow(16,12,11)}')

```
> ## 22. Async Await 
```python
        import asyncio
        import time

        async def PrintSomething():
            print("Hello ")
            # asynchronous way of sleeping, await functionName/operation will do
            await asyncio.sleep(2)
            print("World")

        asyncio.run(PrintSomething())
        # synchronous way of sleeping
        time.sleep(2)
        print("How are you ?")
```
> ## 23. Calculating Execution time of a program
```python
        import time 

        start=time.time() # note down the current time

        j=0
        for i in range(100000):
            j +=1

        end=time.time() # note down time right now

        print(f'Difference of time in seconds : {end-start}')
        print(f'Difference of time in miliseconds : {(end-start)*1000}')
```
