from random import randint


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    tiles_in_hand = []

    def draw(self, tiles_sack):
        if len(self.tiles_in_hand) < 7:
            index = randint(0, len(tiles_sack))
            tile_to_draw = tiles_sack.pop(index)
            self.tiles_in_hand.append(tile_to_draw)
