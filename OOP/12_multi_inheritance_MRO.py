""" 
    MRO = Method Resolution Order. As python supports multi-inheritance so whenever python inherits many classes and
    if they have same method then python resolves those method orders so that compiler can decide which method to call
    in run time  like below

        Dymond problem :
        class A   class A
            ⬇️          ⬇️
        class B   class C
            ⬇️          ⬇️
        class D   class D
    If A,B,C have a same named method then instance of class D will call which class method ?

    MRO (Method Resolution Order) known from D.mro() explain this for scenario below
        class D
            ⬇️
        class B
            ⬇️
        class C
            ⬇️
        class A
    that means firstly python will search for same named method implementation in D, then B -> C -> A
 
 """

class A:
    def say_greet(self):
        print('Hi from A')
    
class B(A):
    def say_greet(self):
        print('Hi from B')
    # pass

class C(A):
    def say_greet(self):
        print('Hi from C')
    # pass

class D(B, C):
    def say_greet(self):
        print('Hi from D')
    # pass

d = D()

print(D.mro())
print(D.__mro__)
# shows order of MRO
help(D)

d.say_greet()