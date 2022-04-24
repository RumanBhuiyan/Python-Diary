from types import SimpleNamespace


point1 = SimpleNamespace(x=2.5,y=3.1,z=4.6)

# SimpleNamespace is mutable so you can change its value anytime 
point1.x = 2.99

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print(f"z = {point1.z}")