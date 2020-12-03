# python supports multi-class-inheritance
class Bird:
    def fly(self):
        print('It can fly')


# class Hen(Bird):  # inheriting Bird class
# calling parent class constructor : Bird.__init__() or super().__init__()
#     pass
class Hen:

    def swim(self):
        print('It can swim')


class Duck(Bird, Hen):
    pass


print('Duck : ')
newDuck = Duck()
newDuck.fly()
newDuck.swim()
