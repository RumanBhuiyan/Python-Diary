# decorator takes a callable & returns another callable

def wrapper1(func):
    def say_hi():
        message = func() + " Hi"
        return message
    return say_hi


def wrapper2(func):
    def say_bye():
        message = func() + " Bye"
        return message
    return say_bye
    

@wrapper2
@wrapper1
def greet():
    return "Hello "

print(greet()) # Output : Hello  Hi Bye