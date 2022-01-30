# if you run python file with -O flag then assertion error willn't come
# def summation_of_age(a,b):
#     assert a>0 and b> 0 , "Age can't be negative"
#     return a+b

# print(summation_of_age(-2,4))

# doctest
# running command in terminal :  python -m doctest -v .\Testing.py
def get_sum(a,b):
    """ writing test for this function
    >>> get_sum(2,4)
    6
    >>> get_sum(2,3)
    5
    """
    return a+b