# difference between len() __len__() is len() searchs for you own 
# implementation of __len__() inside object then call it . If not found
# calls built-in len()
numbers = [1,2,3,4,5]

print(len(numbers))
print(numbers.__len__())

# defining our own len function 
class hello:
    def __init__(self,value):
        self.name = value
    
    def __len__(self):
        return 50


h = hello('ruman')
print(h.__len__())
print(len(h))
