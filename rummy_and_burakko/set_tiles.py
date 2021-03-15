class SetTiles():
    def __init__(self, *args):
        self.tiles = []
        for t in args:
            self.tiles.append(t)

    # create an atribute containing the tiles
    def is_valid(self):
        return self.is_a_leg() or self.is_a_stair()

    def is_a_leg(self):
        return True

    def is_a_stair(self):
        return False

