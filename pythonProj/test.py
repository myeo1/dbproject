class Car:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour
    def describe(self):
        print(f'My car is a {self.colour} {self.model}.')

my_car = Car('Toyota','blue')
my_car.describe()

class Car:
    def __init__(self, model, colour, fuel):
        self.model = model
        self.colour = colour
        self.fuel = fuel
    def describe(self):
        print(f'My car is a {self.colour} {self.model}.')
    def refuel(self):
        self.fuel = self.fuel + 50
    def getfuel(self):
        return self.fuel

my_car = Car('Toyota','blue', 10)
my_car.getfuel()
my_car.refuel()
my_car.refuel()
my_car.getfuel()

class Van(Car):
    def __init__(self, model, colour, fuel, capacity):
        super().__init__(model, colour, fuel)
        self.capacity = capacity
    def describe(self):
        print(f'My van is a {self.colour} {self.model}.')
    def is_van(self):
        return True
    def get_capacity(self):
        return self.capacity

my_van=Van('Suzuku','White',50,300)
my_van.is_van()
my_van.get_capacity()
my_van.getfuel()
my_van.describe()
