# Throwing Error

# process 01 : if condition becomes false then message is displayed 
number = -2
assert (number > 0), "Number should be positive"

# process 02 :
# we can handle assertion error by using Exception like below
number = -5
if number < 0 :
    raise Exception("Number shoul be positive") 
