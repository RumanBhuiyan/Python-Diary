#practise iterator 
# () is optional in class declaration in python
class myList():
    def __init__(self,nums):
        self.numbers = nums
        print(f'constructor of myList class is called. now self.numbers = {self.numbers}')
    
    def __iter__(self):
        print(f'__iter__ method of myList class is called')
        self.iterator = iter(self.numbers)
        return self
    
    def __next__(self):
        # process - 01 
        # print(f'__next__ of myList is called')
        # return next(self.iterator)
        # at end of iteration print() will be executed and next(self.iterator) will throw StopIteration
        # thats why for loop will be terminated.

        # process - 02
        try:
            value = next(self.iterator)
        except:
            # throwing StopIteration error  because for loop will terminate just because of it
            raise StopIteration
        else:
            print(f'__next__ method of myList class is called')
            return value



numbers = myList([1, 2, 3, 4, 5])

# accessing values,
for num in numbers:
    print(num)


# accessing values
it = iter(numbers)
while True:
    try:
        value = next(it)
    except StopIteration:
        break
    else:
        print(value)
