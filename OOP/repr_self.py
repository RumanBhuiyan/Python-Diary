class hudai:
    def __init__(self,fname,lname) :
        self.fname = fname
        self.lname = lname

    # this is the representation of object of this class
    def __repr__(self) :
        return f"First Name : {self.fname} Last Name : {self.lname}"
    
    def get_details(self):
        print(self)

  
h = hudai("Ruman","Bhuiyan")

# when i will try to print h then python will serach for h class representation
# method to know about how to print it
print(h)

# look self is also refering to __repr__() method of the class
h.get_details()