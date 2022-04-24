class A:
    def __init__(self, name):
        self.name = name
        print(f'Class A constructor initiated self.name = {self.name}')

class B:
    def __init__(self, name):
        self.name = name
        print(f'Class B constructor initiated self.name = {self.name}')

class C(A, B):
    def __init__(self, name):
        # According to MRO super -> A class 
        super().__init__(name)
        
        # if super() is confusing or you wanna call any class constructor denying MRO Rules then
        # call constructor like below
        B(name)


c = C('Bohemians')
