from random import randint

class Die:
    def __init__(self, sides):
        self.sides = 6
    def roll_die(self, sides):
        self.sides = randint(1,self.sides) 
        print(self.sides)

mydie = Die(6)
mydie.roll_die(2)
