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
        # Evitamos que tomemos como ref a un joker
        for tile in self.tiles:
            if tile.number != 0:
                reference = tile.number
                break
        same_digit = all(
            obj.number == reference
            for obj in self.tiles
            if obj.is_joker is False
        )

        return dif_color and same_digit

    def is_a_stair(self):
        number = sorted(list([t.number for t in self.tiles]))
        size = len(number)
        joker_tiles_quantity = number.count(0)
        if size < 3 or size > 13:
            return False
        for i in range(size - 1):
            if number[i] != number[i + 1] - 1 and number[i] != 0:
                if joker_tiles_quantity > 0:
                    joker_tiles_quantity - 1
                else:
                    return False
        colors = list([c.color for c in self.tiles])
        if colors.count('*') == 1:
            if colors[0] == '*' and colors.count(colors[1]) == len(colors) - 1:
                return True
            elif colors.count(colors[0]) == len(colors) - 1:
                return True
        elif colors.count('*') == 0 and colors.count(colors[0]) == len(colors):
            return True
        else:
            return False

    def remove_tile(self, tile):
        self.tiles.remove(tile)

    def get_tiles(self):
        set_type = ''
        if self.is_a_leg():
            set_type += 'L'
        elif self.is_a_stair():
            set_type += 'S'
        else:
            set_type += 'Wrong'
        return (
            set_type + '[ '
            + ' '.join([
                f'{index}:{tile.color}{tile.number}'
                for index, tile in enumerate(self.tiles)
            ])
            + ' ]'
        )

    def extract_one_tile(self, index):
        try:
            return self.tiles.pop(index)
        except IndexError:
            raise IndexError

    def put_tile(self, tile, index):
        self.tiles.insert(index, tile)
