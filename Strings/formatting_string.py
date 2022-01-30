from string import Template


first_name = 'Ruman'
last_name = 'Bhuiyan'

# process : 01 (old way of formatting) both available in python 2 & python 3
print("So you are %s %s"%(first_name,last_name))

# process : 02 using format() both available in python 2 & python 3
print("so you are {0} {1}".format(first_name,last_name))

# process : 03 using f string only available in python 3
print(f'so you are {first_name} {last_name}')
# %r is used as debug tracer in formatting 
print("firstname : %r lastname : %r"%(first_name,last_name))

# process : 04 (used for user formatted strings)
user = Template('So you are $first_name $last_name')
user = user.substitute(first_name='Elon',last_name='Mask')
print(user)