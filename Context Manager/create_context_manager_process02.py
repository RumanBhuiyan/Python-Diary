# process : 02 (creating own context manager using functional approach)
from contextlib import contextmanager


@contextmanager
def open_my_file(filename,filemode):
    file = open(filename,filemode)
    yield file
    file.close()


with open_my_file('context_functions.txt','w') as my_file:
    my_file.write('context function contents...')


# lets check whether file closed or not
print(f'my_file closed ? {my_file.closed}')