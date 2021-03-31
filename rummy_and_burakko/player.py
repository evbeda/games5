class Player:
    def __init__(self, name):
        self.name = name
        self.first_move = True
        self.hand = []
        self.temp_hand = []
        self.is_playing = False

    def add_tiles(self, tiles):
        if self.is_playing:
            self.temp_hand += tiles
        else:
            self.hand += tiles

    def remove_tile(self, index):
        self.temp_hand.pop(index)

    def get_a_tile(self, index):
        return self.temp_hand[index]

    def get_hand(self):
        return f'{self.name}> ' + ' '.join([
            f'{index}:{tile.color}{tile.number}'
            for index, tile in enumerate(self.temp_hand)
        ])

    def temporary_hand(self):
        self.temp_hand = self.hand.copy()

    def valid_hand(self):
        if len(self.hand) <= len(self.temp_hand):
            return False
        return True

    def validate_turn(self):
        self.hand = self.temp_hand.copy()

    def change_state(self):
        self.is_playing = not self.is_playing

    def get_lenght(self):
        return len(self.temp_hand)

    def change_first_move(self):
        if self.first_move:
            self.first_move = False

    def get_first_move(self):
        return self.first_move

    def has_tiles(self):
        return (len(self.hand) > 0)

    def tiles_in_hand(self, *indexes):
        return (
            True if max(indexes) < len(self.temp_hand)
            else False
        )
