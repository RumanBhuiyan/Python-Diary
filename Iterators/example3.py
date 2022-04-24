# lets make clone of range() in python in our own way
class my_range:
    def __init__(self,limit):
        # decrease self.index value by 1 as its value will be increase inside __next__(self) again
        self.index = -1
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        # check before returning that whether the value satisfies the range or not
        if self.index + 1 < self.limit:
            # if the statement below goes below return statement then this will be un-reachable
            self.index += 1
            return self.index
        else :
            raise StopIteration

# lets make our own way of range(start,stop,step) in our own way
class my_range2:
    def __init__(self,start, stop, step = 1):
        # decrease self.start value by self.step as it will be increased inside __next__(self) again
        self.start = start - step
        self.stop = stop 
        self.step = step
    
    def __iter__(self):
        return self
    

    def __next__(self):
        # check before returning that whether the value satisfies the range or not
        if self.start + self.step < self.stop:
            self.start += self.step
            return self.start
        else:
            raise StopIteration


for num in my_range(5):
    print(num)

for num in my_range2(20,100,10):
    print(num)