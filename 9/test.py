class Car:

    def __init__(self, make, model, year):
        """initialize the car class"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement about the car milage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Set the odomoter reading to the given value"""
        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        """add miles to odomoter"""
        self.odometer_reading += miles
class ElectricCar(Car):
    """Represent electric cars"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        """Print a statement about the battery size"""
        print(f"This car has a {self.battery_size}-kwh battery")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



