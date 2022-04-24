# exc_info helps us to get information about last throwing error
from sys import exc_info

# lets make my own join implementation
class my_string:
    def __init__(self, delimiter):
        self.delimiter = delimiter
    
    def join(self, items):
        temp = ''
        try:
            _ = iter(items)
        except:
            # exc_info() provides info as tuple only inside except block
            print(exc_info()[1])
            
            # exc_type, exc_value, exc_tb = sys.exc_info()
            # tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
            # return tb
        else:
            for item in items:
                temp += self.delimiter + str(item) if len(temp) else str(item)
        return temp



my_del = my_string(',')
print(my_del.join([1,2,3,4]))
print(my_del.join(12))

