class myDict(dict):
    def __init__(self):
        self.words = dict()
        print("New dictionary Initiated!!")

    # --len__ are called Dunder methods Double underscore shorts Dunder
    def __len__(self) :
        print("you asked for length")
        return super().__len__() # calling dict class __len__ method
    
    def __setitem__(self,key,value):
        super().__setitem__(key,value) # calling dict class __setitem__ method
        print("New item inserted into dictionary")

#help(dict)
keep = myDict()
print(len(keep))
# myDict class __setitem__() will be called now
keep['Ruman'] = 23
# myDict class __len__() method will be called now
print(len(keep))
