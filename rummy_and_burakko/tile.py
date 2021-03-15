class Tile():
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.is_joker = not(
            self.color != '*' and self.number != 0
        )
