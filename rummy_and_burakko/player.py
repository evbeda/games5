class Player:
    def __init__(self, name):
        self.name = name
        self.first_move = True
        self.hand = []
        self.temp_hand = []

    def add_tiles(self, tiles):
        self.hand += tiles

    def remove_tiles(self, tiles):
        for tile in tiles:
            if tile in self.hand:
                self.hand.remove(tile)
            else:
                raise Exception

    def get_hand(self):
        return f'{self.name}> ' + ' '.join([
            f'{index}:{tile.color}{tile.number}'
            for index, tile in enumerate(self.hand)
        ])

    def temporary_hand(self):
        self.temp_hand = self.hand.copy()

    # valida si tengo menos fichas que antes y ni una nueva ficha en mano
    def valid_hand(self):
        if len(self.hand) <= len(self.temp_hand):
            return False
        count = 0
        h_tiles_comp = self.hand.copy()
        for t_tile in self.temp_hand:
            for h_tile in h_tiles_comp:
                if t_tile.color == h_tile.color and t_tile.number == h_tile.number:
                    h_tiles_comp.remove(h_tile)
                    count += 1
                    break
        if count == len(self.temp_hand):
            return True
        else:
            return False

    def valid_turn(self):
        self.hand = self.temp_hand.copy()
