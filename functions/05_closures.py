# clousures are such functions which can memorise a state/variable in every call
# in other words we can embed any resource with function for later calls in closures

# lets look into an  example of closure
def add_one(initial = 0):
    summation = initial

    def plus_one(num):
        nonlocal summation
        summation += num
        return summation
    
    return plus_one

increase = add_one()
print(increase(10))
print(increase(10))

increase = add_one(11)
print(increase(2))
print(increase(3))


# let's look into another example of closure
def collect_even_numbers(even_numbers = []):

    def is_even(number):
        if number %2 == 0:
            even_numbers.append(number)
        return even_numbers
    
    return is_even

check_and_get_even_numbers = collect_even_numbers()

for i in range(1,12):
    print(check_and_get_even_numbers(i))
