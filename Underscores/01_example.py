from typing import NamedTuple

class Person(NamedTuple):
    name : str
    age : int
    roll : int

ruman = Person('Ruman',24,76)

# _ is used where i dont care about the name of variable
_,age,roll = ruman

print(age)
print(roll)


#As _ doesn't mean anything to us but we can use _ as a normal variable like below
_ = [1,2,3,4,5]

print(_)

_.append(6)
print(_)