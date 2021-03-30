class Spot:
    def __init__(self, mult_value, mult_type):
        self.tile = None
        self.mult_value = mult_value
        self.mult_type = mult_type
        self.mult_not_used = True

    def set_tile(self, tile):
        self.tile = tile

    def get_spot(self):
        return (
            f' {self.tile.letter} '
            if self.tile else
            f'{self.mult_value}x{self.mult_type.upper()}'
            if self.mult_value else '   '
        )
