# thus we can implement abstraction & interfaces
from abc import abstractmethod,ABC

class Animal(ABC):
    species = 'animal'

    @abstractmethod
    def eat():
        pass

    @abstractmethod
    def speak():
        pass


class Dog(Animal):
    def eat(self):
        print('Dog eats meat rice etc')
    
    def speak(self):
        print('Dog speaks gheu gheu')


dog = Dog()
print(f'Dog species : {dog.species}')
dog.eat()
dog.speak()