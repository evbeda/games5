class Tile():
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.is_joker = (False if self.color != '*'
                         and self.number != 0 else True)
