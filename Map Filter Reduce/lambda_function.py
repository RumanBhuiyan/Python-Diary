# if you need a function for 1 time use only then make it lambda
# otherwise if you need a function for using again & again then define it first
def square(number) :
    return number * number

def square2(number) : return number*number

# lambda arguments : expression 
# as lambda function is known as un-named function
# so lets keep it reference to another variable to call it
square3 = lambda number : number * number

print(square(3))
print(square2(4))
print(square3(5))

# lets see lambda in real life action
def get_function(operator):
    if operator == '+':
        return lambda a,b : a+b
    elif operator == '-':
        return lambda a,b : a-b
    elif operator == '*':
        return lambda a,b : a*b
    elif operator == '%':
        return lambda a,b : a%b
    else :
        return lambda : print("provide valid input")

operator = input("Enter + or - or * or % :")
my_func = get_function(operator)

a = int(input("First number : "))
b = int(input( "second number : "))

print(f"Result is {my_func(a,b)}")