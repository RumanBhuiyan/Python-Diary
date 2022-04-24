def get_operation(operator):
    if operator == '+':
        return lambda a,b : a+b
    elif operator == '-':
        return lambda a,b : a - b
    elif operator == '*':
        return lambda a, b : a * b
    elif operator == '/':
        return lambda a,b : a / b
    elif operator == '%':
        return lambda a, b : a % b
    else:
        return lambda *args : 'Operator unknown'


# better implementation - 02
def get_operation2(operator):
    return {
        '+' : lambda a, b : a + b,
        '-' : lambda a, b : a - b,
        '*' : lambda a, b : a * b,
        '/' : lambda a, b : a / b,
        '%' : lambda a, b : a % b,
    }[operator] if operator in ['+','-','*','/','%'] else lambda *args : 'Operator unknown'


# better implementation - 03
def get_operation3(operator):
    functions = {
        '+' : lambda a, b : a + b,
        '-' : lambda a, b : a - b,
        '*' : lambda a, b : a * b,
        '/' : lambda a, b : a / b,
        '%' : lambda a, b : a % b,
    }
    return functions.get(operator) if functions.get(operator) else lambda *args : 'Operator unknown'

    

print(f"Summation : {get_operation('+')(2,3)} ")
print(f"{get_operation('')(2,3)}")

print(f"Summation : {get_operation2('+')(2,3)} ")
print(f"{get_operation2('')(2,3)}")

print(f"Summation : {get_operation3('+')(2,3)} ")
print(f"{get_operation3('')(2,3)}")