class SetTiles():
    def __init__(self, tiles):
        self.tiles = tiles.copy()

    # create an atribute containing the tiles
    def is_valid(self):
        return self.is_a_leg() or self.is_a_stair()

    def is_a_leg(self):
        colors = set([c.color for c in self.tiles])
        if len(colors) < 3 or len(colors) > 4:
            return False
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
        number = sorted(list([t.number for t in self.tiles]))
        size = len(number)
        if size < 3 or size > 13:
            return False
        for i in range(size-1):
            if number[i] != number[i+1]-1:
                if number[i] != 0:
                    return False
        colors = list([c.color for c in self.tiles])
        if colors.count('*') == 1:
            if colors[0] == '*' and colors.count(colors[1]) == len(colors)-1:
                return True
            elif colors.count(colors[0]) == len(colors)-1:
                return True
        elif colors.count('*') == 0 and colors.count(colors[0]) == len(colors):
            return True
        else:
            return False
