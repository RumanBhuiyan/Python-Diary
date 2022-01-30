from typing import NamedTuple


class Point(NamedTuple):
    x : float
    y : float
    z : float


point1 = Point(1.2,2.5,3.4)

# but namedTuple immutable which means it doesn't allow item re-assignment
# point1.x = 5.5

print(f"x = {point1.x}")
print(f"y = {point1.y}")
print(f"z = {point1.z}")