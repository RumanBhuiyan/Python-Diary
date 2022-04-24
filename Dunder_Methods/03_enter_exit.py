"""
    __enter__() method is used at the time of creating own context manager and it is called
    by as operator like below. __exit__() is called by python when execution come out of
    context manager scope . Finally __enter__() and __exit__() these 2 dunder methods 
    helps us to create context manager.
"""


# example below took from python tips and trips book
class Indenter:
    def __init__(self):
        # print('constructor called...')
        self.level = 0
    
    def __enter__(self):
        # print('__enter__() called')
        self.level += 1
        return self
    
    def __exit__(self,exc_type, exec_value, exec_tb):
        # print('__exit__() called')
        self.level -= 1
    
    def print(self, text):
        print('    '*self.level,text )


with Indenter() as indent: # calls __init__() -> __enter__()
    indent.print(f'Hi! level = {indent.level}')
    with indent: # calls __enter__()
        indent.print(f'Hello!! level = {indent.level}')
        with indent: # calls __enter__()
            indent.print(f'Ruman!!! level = {indent.level}')
        # calls __exit__()
    # calls __exit__()
    indent.print(f'Bye! level = {indent.level}')
    # calls __exit__()