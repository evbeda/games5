class Player:
    def __init__(self, name):
        self.name = name
        self.first_move = True
        self.hand = []

    def add_tiles(self, tiles):
        self.hand += tiles

    def remove_tiles(self, tiles):
        for tile in tiles:
            if tile in self.hand:
                self.hand.remove(tile)
            else:
                raise Exception

