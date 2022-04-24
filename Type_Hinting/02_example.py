def factorial_of(number : int) -> int :
    product : int = 1
    while number > 1:
        product *= number
        number -= 1
    return product


print(factorial_of(5))

# N.B => code below wont throw error though
print(factorial_of(5.5))
