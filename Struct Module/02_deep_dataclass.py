from dataclasses import dataclass, astuple, asdict

# init = True means generate __init__() for class Point
# order = True implements __eq__, __lt__ etc comparing methods for us

@dataclass (init= True, order = True)
class Point:
    x : float
    y : float
    z : float = 0.0

    @staticmethod
    def slope(p1, p2):
        return round((p1.y - p2.y)/(p1.x -p2.x),3)


p1 = Point(1.1,2.1)
p2 = Point(1.1,2.1)
p3 = Point(1.2,2.2,1.5)

print(p1 == p2)
print(p1 < p3)

# astuple() converts any dataclass object into tuple
print(astuple(p1))

# asdict() converts any dataclass object into dictionary
print(asdict(p1))

print(Point.slope(p2,p3))