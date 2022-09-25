from random import randint

class Die:
    def __init__(self, sides):
        self.sides = 6
    def roll_die(self):
        roll=randint(0, self.sides)
        print(roll)

die1= Die(10)
die2= Die(20)

for i in range(10):
    die1.roll_die()
    die2.roll_die()
