class Spot:
    def __init__(self, mult_value, mult_type):
        self.tile = None
        self.mult_value = mult_value
        self.mult_type = mult_type

    def set_tile(self, tile):
        self.tile = tile

    def get_spot(self):
        return f' {self.tile.letter} ' if self.tile else f'x{self.mult_value}{self.mult_type}' if self.mult_value else '   '
