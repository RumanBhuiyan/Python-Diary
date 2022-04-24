# decorator is a function which takes a function as an argument &
# returns another function after adding functionality  to it
# a decorator is a callable that takes a callable as input and returns another callable.
def print_name(get_name):
    def print_fullname():
        name = get_name()
        print(f"So you are {name}")
        print(f"Hello {name}")
    return print_fullname

def name():
    return 'Ruman'

# process - 01 : calling and using decorator
bio = print_name(name)
bio()


# process - 02 : short syntax for decorator
@print_name
def send():
    return "Buman"
send()
# this is similar as send = print_name(send)

