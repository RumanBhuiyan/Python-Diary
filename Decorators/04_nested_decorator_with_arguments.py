def print_summation(summation):
    
    def print_summation_wrapper(*args):
        print(f'Summation is {summation(*args)}')
    
    return print_summation_wrapper


def get_summation(summation):

    def get_summation_wrapper(*args):
        return summation(*args)
    
    return get_summation_wrapper


@print_summation
@get_summation
def total_summation(*args):
    summation = 0

    for number in args:
        summation += number
    return summation


total_summation()
total_summation(1, 2, 3, 4, 5)

# this is example what i picked from my thought. Just think how its working under the hood.
# Behind scene is amazing