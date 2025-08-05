from abc import ABC, abstractmethod
class Vechicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vechicle):
    def go(self):
        print("YOU DRIVE THE CAR")
    def stop(self):
        print("THIS CAR IS STOPPED")
car=Car()
print(car.go())