# MRO = Method Resolution Order
# as python supports multi-inheritance so whenever python inherits many classes and
# if they have same method then python resolves those method orders so that
#  compiler can decide which method to call in run time  
class A :
    def print_className(self):
        print("Class Name A")

class B(A) :
    def print_className(self):
        print("Class Name B")

class C(A) :
    def print_className(self):
        print("Class Name C")

class D(C,B):
    pass
    # def print_className(self):
    #     print("Class Name D")

# built in utilities for knowing methods order 
# print(D.__mro__)
#print(D.mro())
help(D)
# output
# Method resolution order:       
#  |      D
#  |      C
#  |      B
#  |      A
#  |      builtins.object
# this order says that, first of all python will call the overriden function of 
# print_className() inside class D. If not found then look into class C. If not found
# there then look into class B and so on.

# tips 
# dont call parent constructor like this : super.__int__(name,value)
# rather call it like : A.__init__(name,value)
# in case of multi-inheritance super.__init__() becomes ambiguous to us
d = D()
d.print_className()