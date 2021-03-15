class SetTiles():
    def __init__(self, tiles):
        self.tiles = tiles.copy()

    # create an atribute containing the tiles
    def is_valid(self):
        return self.is_a_leg() or self.is_a_stair()

    def is_a_leg(self):
        colors = set([c.color for c in self.tiles])
        dif_color = len(colors) == len(self.tiles)
        # optimizar esta linea para solucionar error joker
        reference = (sorted(
            list(t.number for t in self.tiles), reverse=True))[0]
        same_digit = all(
            obj.number == reference
            for obj in self.tiles
            if obj.is_joker is False
        )

        return dif_color and same_digit

    def is_a_stair(self):
        return False

