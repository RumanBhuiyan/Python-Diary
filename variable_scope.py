# https://www.datacamp.com/community/tutorials/scope-of-variables-python?msclkid=d2f5083da5c311ecad67e93c331c6139

def A():

    # show me gloabl scoped  variables and methods
    print(globals())

    # now local_price, local_numbers are in local scope
    local_price = 500
    local_numbers = [21,22,23,24,25]

    # show me local scoped variables and methods
    print(locals())

    B()


def B():
    print(globals())
    print(locals())



if __name__ == '__main__':

    # Now global_price,global_numbers are in global scope
    global_price = 100
    global_numbers = [1,3,4,5]

    A()