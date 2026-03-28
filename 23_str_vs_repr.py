#!/usr/bin/env python3


class MyClass:
    def __str__(self):
        return "__str__: Human-readable"

    def __repr__(self):
        return "__repr__: Developer-readable"


obj = MyClass()

# let's check whom object calls itself
print(f"obj: {obj}")

# str()
print(f"str(obj): {str(obj)}")  # Output: Human-readable
print(f"obj.__str__(): {obj.__str__()}")  # Output: Human-readable

# repr()
print(f"repr(obj): {repr(obj)}")  # Output: Developer-readable
print(f"obj.__repr__(): {obj.__repr__()}")  # Output: Developer-readable

# that means
# str representation need? str -> repr -> none
# str() called?  →  __str__ defined?  →  use it
#                         ↓ No
#                __repr__ defined?  →  use it
#                         ↓ No
#                default object repr (e.g. <__main__.MyClass object at 0x...>)

