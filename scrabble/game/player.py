import random


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.tiles_in_hand = []

    def one_draw(self, tiles_sack):
        index = random.randint(0, len(tiles_sack.tiles)-1)
        tile_to_draw = tiles_sack.draw_tile(index)
        self.tiles_in_hand.append(tile_to_draw)

    def full_draw(self, tiles_sack):
        diff = 7 - len(self.tiles_in_hand)
        # Por si quedan menos fichas en el pozo que diff
        if diff > len(tiles_sack.tiles):
            diff = len(tiles_sack.tiles)
        while diff != 0:
            self.one_draw(tiles_sack)
            diff -= 1

    def put_t_draw_t(self, tiles_sack, indexs):
        indexs.sort(reverse=True)
        for index in indexs:
            tile = self.tiles_in_hand.pop(index)
            tiles_sack.add_tile(tile)
            # tiles_sack.append(tile)
        self.full_draw(tiles_sack)

    def get_hand(self):
        pass
