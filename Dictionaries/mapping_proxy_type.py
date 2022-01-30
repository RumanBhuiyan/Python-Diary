# we can make any dictionary read-only using MappingProxyType
from types import MappingProxyType


numbers = {"one" : 1, "two" : 2, "Three": 3}
print(numbers)

numbers["Four"] = 4
print(numbers)

numbers = MappingProxyType(numbers)
numbers["Five"] = 5 # throws error