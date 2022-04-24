# mixins used in python to add extra methods with a class without changing that class to create a new class
# mixins help us to avoid dymond problem in multi-inheritance becuase using mixins to acheive our purpose
# helps us to control the flow rather then depending on python MRO

class Car:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def show_price(self):
        print(self.price)

class discount_car:
    def get_price_with_discount(self):
        return round(self.price - (self.price * 40)/100,3)
    
    def loan_per_month(self, year):
        return round(self.price/(year * 12),3)


# mixins classes are evaluated from Right to left
class Tesla(discount_car, Car):
    pass

mycar = Tesla("Test Road star",20_000)
mycar.show_price()

print(mycar.get_price_with_discount())
print(mycar.loan_per_month(3))
