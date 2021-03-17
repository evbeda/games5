class Spot:
    def __init__(self, mult_value, mult_type):
        self.tile = None
        self.mult_value = mult_value
        self.mult_type = mult_type

    def set_tile(self, tile):
        self.tile = tile
