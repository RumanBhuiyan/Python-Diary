class my_loop:
    def __init__(self,args):
        self.numbers = args
    
    def __iter__(self):
        return iter(self.numbers)
    
    def __next__(self):
        return next(self.numbers)

# process : 01 (writting custom loop)
another = my_loop([6,7,8,9,10])
another_iterator = iter(another)
for num in another_iterator:
    print(num)


# Process : 02 writting custom loop 
numbers = [1,2,3,4,5]
iterator = iter(numbers)

while True:
    try:
        item = next(iterator)
    except :
        break
    else:
        print(item)
