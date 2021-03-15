import random


class Die:

    def __init__(self, color):
        self.color = color

    def roll_die(self):
        return random.randint(1, 6)
