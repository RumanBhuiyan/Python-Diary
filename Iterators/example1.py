# practise iterator 
class myList:
    def __init__(self,nums) :
        self.numbers = nums
        print(f'myList constructor is called and now self.numbers = {nums}')
    
    def __iter__(self):
        print(f'__iter__ of myList class is called')
        return  iter(self.numbers)
        # as i am returning iterator of self.numbers, which isn't object of myList class rather a property of myList class
        # that's why that iterator object wont have __next__(self) implementation of this class. As a result, python will call
        # next() of python own implimentation. So __next__(self) method below wont get called by python compiler.
    
    def __next__(self):
        print(f'__next__ of myList class is called')
        return next(self.iterator)



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
