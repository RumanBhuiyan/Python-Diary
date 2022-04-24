def get_first_name(first_name):

    def first_name_wrapper():
        return f'Hello {first_name()}'
    
    return first_name_wrapper


def get_second_name(fname):

    def second_name_wrapper():
        return f'{fname()} How are you ?'
    
    return second_name_wrapper


# process - 01:
@get_second_name
@get_first_name
def fname():
    return "Ruman"

print(fname())

# process - 02
@get_first_name
@get_second_name
def fname():
    return "Bhuiyan"

print(fname())
