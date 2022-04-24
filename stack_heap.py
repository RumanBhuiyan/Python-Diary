def A():
    print(f'From A -> Price : {price}')
    print(f'From A -> Numbers : {numbers}')

    # priceA, NumbersA are inside only A() not in main stack
    # thats why B() can't access them
    priceA = 12000
    NumbersA = [21, 22, 23]

    B()


def B():
    print(f'From B -> Price : {price}')
    print(f'From B -> Numbers : {numbers}')

    # throw error because 
    # print(f'From B -> PriceA : {priceA}')
    # print(f'From B -> NumbersA : {numbersA}')



if __name__ == '__main__':

    # Now price , numbers are in main stack 
    price = 10000
    numbers = [1, 2, 3, 4, 5]

    # A() is pushed onto stack so it can access price, numbers
    A()
