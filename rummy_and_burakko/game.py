class Game():
    def __init__(self, n):
        self.remaining_pieces = []
        self.players = ''
        self.actual_turn = int

    def create_pieces():
        colors = ('r', 'b', 'w', 'y')
        pieces = []
        for color in colors:
            for number in range(1, 14):
                piece = color + str(number)
                pieces.append(piece)

        pieces = pieces + pieces.copy()
        jokers = ['*', '*']
        return pieces + jokers



