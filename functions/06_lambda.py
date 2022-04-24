# lambda means one statement functions that means that every lambda function should have one statement in its body
is_even = lambda x : x%2 == 0
is_divisor = lambda x,y : f"{y} is divisor of {x}" if x % y == 0 else f"{x} is divisor of {y}" if y % x == 0 else "None of them are divisor of each other"

print(is_even(4))
print(is_divisor(2,4))
print(is_divisor(4,2))
print(is_divisor(3,7))