class Restaurant:
    """A simple attempt to model a Restaurant"""

    def __init__(self, name, cusine):
        """Initialize attributtes"""
        self.name = name
        self.cusine = cusine
        self.number_served = 0
    def describe_restaurant(self):
        """Describe the Restaurant"""
        print(f"This Restaurant is called {self.name.title()} and serves {self.cusine} food")
    def open_restaurant(self):
        """Show if the restaurant is open"""
        print(f" {self.name.title()} is open please come in!")
    def show_customers(self):
        print(f"The {self.name.title()} restaurant has served {self.number_served}")
    def add_customers(self, served):
        self.number_served += served

class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""
    def __init__(self, name, cusine='ice_cream'):
        super().__init__(name, cusine)
        self.flavours = []
    def show_flavours(self):
        print("\n We have the following flavours avalible:")
        for flavour in self.flavours:
            print(f"-{flavour.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavours=['vanilla','chocolate','black cherry']
big_one.describe_restaurant()
big_one.show_flavours()
