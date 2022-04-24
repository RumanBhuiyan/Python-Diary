"""
    I have tried to implement my own defaultdict implementation from my knowledge of python
    i got to know about __getitem__ , __setitem__ by dir(dict). After knowing about them
    i constructed the solution below

    __getitem__ is called when numbers[key] 
    __setitem__ is called when numbers[key] = value

    Really how amazing the dunder methods are!! that's why those are called magic methods, probably
"""
class my_defaultdict:
    def __init__(self, func_name):
        self.default_func = func_name
        self.my_dict = dict()

    def __getitem__(self, key):
        print(f'__getitem__ of my_dict called')
        return self.my_dict.setdefault(key, self.default_func())
    
    def __setitem__(self, key, value):
        print(f'__setitem__ of my_dict called')
        self.my_dict[key] = value
    
    def __repr__(self):
        print(f'__repr__ of my_dict called')
        return str(self.my_dict)

    def __len__(self):
        print(f'__len__ of my_dict called')
        return len(self.my_dict.keys())

    

numbers = my_defaultdict(int)

# calls __repr__ 
print(numbers)
# calls __getitem__ 
print(numbers['One'])
print(numbers)

# set item by using dunder __setitem__
numbers['Two'] = 2
print(numbers)

# getting length of dictionary by __len__
print(len(numbers))