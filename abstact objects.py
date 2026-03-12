from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print(self.brand, self.model, self.year)

class Bike(Vehicle):

    def start(self):
        print("Start with kick")

class Truck(Vehicle):
    def __init__(self, brand, model, year, color):
        self.color = color

    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self, brand, model, year, wheel): <----- This
        self.wheel = wheel

    def start(self):
        print("Start with key")


bike = Bike("Bike1", 2, 2023)
truck = Truck("Truck1", 3,  2023, "red")
car = Car("Car1", 3, 2023, 4) <------- This
  
print(car.year)
print(car.start())
print(bike.start())
print(truck.start())
truck.display()