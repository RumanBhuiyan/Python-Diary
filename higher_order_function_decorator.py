# a function which takes a function as a parameter and return another 
# function that is called higher order function
def get_country(name):

    def print_country() :
        print(f"The country name is {name()}")
    
    return print_country

# process: 01
name = lambda : "Bangladesh"
country = get_country(name)
country()

#process: 02
# below line is similar as  name = get_country(name) 
@get_country
def name():
    return "Canada"

name()
