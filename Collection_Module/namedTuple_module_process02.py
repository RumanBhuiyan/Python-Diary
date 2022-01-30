# this type of namedTuple makes our code more readable & can be used as an alternative
# of class in simple scenario 
from typing import NamedTuple


class Car(NamedTuple):
    name : str
    mileage : float
    price : int


my_car = Car('Tesla Roadstar',25.36 ,50_000)

print(f"Car name : {my_car.name}")
print(f"Car mileage : {my_car.mileage} miles/hour")
print(f"Car price : ${my_car.price}")