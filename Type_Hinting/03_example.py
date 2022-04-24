# As python is a dynamic programming language so you use type hinting though 
# if you assign different type data into a variable it wont throw an error
# this type hinting feature is only availabe in python version >= 3.6
# Some pythonistas(python senior developers) say that for large software this dynamic typing
# creates bug and finding those bugs becomes time confusing often

# So if you want that you program should throw error when type hinting isn't followed then
# you should use an external package called 'mypy'. Firstly install it using pip
# installing command :      pip install mypy 
# for my case        :      python3 -m pip install mypy
# running command    :      mypy python_file_name
# this command will show you all issues where type hinting isn't followed

def factorial_of(number : int) -> int :
    product : int = 1
    while number > 1:
        product *= number
        number -= 1
    return product


print(factorial_of(5))

# this will throw error beacuse of incompatible type float instead of int
print(factorial_of(5.5))
