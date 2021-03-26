class Tile():
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.is_joker = not(
            self.color != '*' and self.number != 0
        )
        self.set_id = 0

    def assign_set_id(self, set_id):
        self.set_id = set_id

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.color == other.color and self.number == other.number
