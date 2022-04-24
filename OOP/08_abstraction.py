# abc => Abstract Base class , KISS => Keep It Simple, Stupid
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name):
        print(f'Animal class constructor called')
        self.name = name
    
    # child class will have to implement this otherwise object of child class can't be created
    @abstractmethod
    def eat(self):
        pass

    # As its a concrete method so child class doesn't need to implement its body again rather can access it
    # if child class implements this then this method will be overriden
    def lives_in(self):
         print(f"{self.name} Lives in land")


class Dog(Animal):

    def __init__(self,name):
        print(f'called from Dog class constructor')
        self.name = name
        super().__init__(name)
    
    def eat(self):
        print(f'{self.name} eats meat, fish etc')
    
    def lives_in(self):
        print(f'called from Dog class')
        # return super().lives_in()
        print(f'{self.name} lives in house')


# Abstract class with only abstract methods is equivalent to interface 
class Bird(ABC):

    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def lives_in(self):
        pass


class Magpie(Bird, Animal):

    """ If two or more inherited class have same named methods then  According to MRO(Method Resolution Order)  
    which class will be inherited first method of that class will be called first. you can't create an object of 
    an abstract class if it has one or more abstract methods that means before creating object of any class implement
    all of its abstract methods
    """

    def __init__(self, name):
        print('Magpie class constructor called')
        self.name = name
        # though Bird class is inherited first, Animal class constructor will be called
        # as __init__() is missing Bird class. Python is smart enough to catch it.
        super().__init__(name)

    def fly(self):
        print(f'{self.name} flies in sky')
    
    def eat(self):
        print(f'{self.name} eats insects')

    def lives_in(self):
        print(f'{self.name} lives in nest')

# d = Dog('puppy')
# d.eat()
# d.lives_in()

# According to MRO
dowel = Magpie('Dowel')
dowel.fly()
dowel.eat()
dowel.lives_in()
