"""
    Let's build useState() hook functionality of React.js library using the concept of closure in python.
    Returning value of useState() must be reference type or it should be passed by reference so that
    any changes in state  by returning function of useState() is reflected in state whenever we consume
    state value.
"""

class data:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return "%s"%(self.value)


def useState(initial = 0):
    state = data(initial)
    
    def wrapper(value):
        state.value = value
    
    return [state, wrapper]


value, setValue = useState(0)

print(value)

setValue(5)
print(value)

setValue(10)
print(value)