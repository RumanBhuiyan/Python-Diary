from dataclasses import dataclass


@dataclass
class Point:
    x : float
    y : float
    z : float = 0.0


point1 = Point(1.2,2.5,3.4)

# data class is mutable 
point1.x = 5.5

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print(f"z = {point1.z}")