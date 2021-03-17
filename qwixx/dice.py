import random


class Dice:
    def __init__(self, color):
        self.color = color

    def roll_dice(self):
        return random.randint(1, 6)
