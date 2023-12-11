from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass


class Car(ABC):
    @abstractmethod
    def acclerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass


class LuxuryCar(Car):
    def accelerate(self):
        print('Accelerating luxury car...')
    
    def brake(self):
        print('Braking luxury car...')
    

class CheapCar(Car):
    def accelerate(self):
        print('Accelerating cheap car...')
    
    def brake(self):
        print('Braking cheap car...')