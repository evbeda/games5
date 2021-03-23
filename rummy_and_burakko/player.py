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
        return self.q_tiles() and self.correct_tiles()

    def correct_tiles(self):
        h_tiles_comp = self.hand.copy()
        for t_tile in self.temp_hand:
            try:
                h_tiles_comp.remove(t_tile)
            except: 
                return False

        return True

    def q_tiles(self):
        l_hand = len(self.hand)
        l_temp = len(self.temp_hand)
        if l_hand <= l_temp:
            return False
        return True

    def validate_turn(self):
        self.hand = self.temp_hand.copy()
