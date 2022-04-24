from typing import List, Tuple, Set, Dict

name : str 
regno : float


name = "Ruman"
regno = 2016331076
country : List[str] = ["Bangladesh", "India", "Canada"]
name_roll : Tuple[str, int] = (("ruman",76),("robiul",79))
roll_number : Set[int] = [1,2,3,4,5]
name_roll_dict : Dict[str,int] = {"ruman": 76, "robiul": 79}

print(f'name : {name}')
print(f'regno : {regno}')
print(f'countries : {country}')
print(f'roll_numbers : {roll_number}')
print(f'name_roll : {name_roll}')
print(f'name_roll_dict : {name_roll_dict}')


# N.B => code below wont throw error though
name = 2016331076
regno = "Ruman"

print(f'name : {name}')
print(f'regno : {regno}')