# class methods vs static methods
class Counter:
    # its shared resource among all instances of this class
    count = 0

    def __init__(self,name):
        print(f'{name} object creating...')
        self.name = name
        Counter.count += 1
    
    # classmethod decorator provides cls to access all shared resources among all objects
    # when you will call Counter.get_condition() then due to . cls = Counter occurs under the hood.
    # I mean cls holds the reference of Counter class
    # thats why you can access all of class shared resources by cls.<variable_name>. also you can
    # create an object like cls(name) like below
    @classmethod
    def new(cls, name):
        return cls(name)

    @classmethod
    def get_condition(cls):
        if cls.count % 2 == 0:
            print(f'Counter class count is {cls.count} which is even')
        else:
            print(f'Counter class count is {cls.count} which is odd')
    
    # static method isn't bind with object. That's why it can't access object properties but
    # it can access shared resources value like below. Static methods are like normal functions
    # except is_counter_even() is only avaiable in Counter namespace not in main namespace.
    @staticmethod
    def is_counter_even():
        return Counter.count % 2 == 0
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    

c1 = Counter('Counter1')
# call class method
c1.get_condition()
# static method can be called using class name or object name like below
print(Counter.is_counter_even())
print(c1.is_even(c1.count))

c2 = Counter('Counter2')
c2.get_condition()
print(Counter.is_counter_even())
print(c2.is_even(c2.count))

c3 = Counter('Counter3')
c3.get_condition()
print(Counter.is_counter_even())
print(c3.is_even(c3.count))

# creating object in another approach
c = Counter.new('Counter 5')
print(c.name)