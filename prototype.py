import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    def __init__(self):
        self.color = None
        self.size = None
        self.price = None

    @abstractmethod
    def clone(self):
        pass


class Car(Prototype):
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price
    
    def clone(self):
        return copy.deepcopy(self)
    

if __name__ == '__main__':
    car = Car('red', 'small', 100)
    print(car.color)
    print(car.size)
    print(car.price)
    print(car)
    another_car = car.clone()
    print(another_car.color)
    print(another_car.size)
    print(another_car.price)
    print(another_car)
    print(car == another_car)
    print(car is another_car)
    print(id(car))
    print(id(another_car))
