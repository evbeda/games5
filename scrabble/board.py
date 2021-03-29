from .spot import Spot
from .tile import Tile
from copy import deepcopy

BOARD_MULT = (
    ((  # Multiplier x2 for letters
        (0, 3), (0, 11),
        (2, 6), (2, 8),
        (3, 0), (3, 7), (3, 14),
        (6, 2), (6, 6), (6, 8), (6, 12),
        (7, 3), (7, 11),
        (8, 2), (8, 6), (8, 8), (8, 12),
        (11, 0), (11, 7), (11, 14),
        (12, 6), (12, 8),
        (14, 3), (14, 11),
    ),
        (2, 'l'),
    ),
    ((  # Multiplier x3 for letters
        (1, 5), (1, 9),
        (5, 1), (5, 5), (5, 9), (5, 13),
        (9, 1), (9, 5), (9, 9), (9, 13),
        (13, 5), (13, 9),
    ),
        (3, 'l')
    ),
    ((  # Multiplier x2 for words
        (1, 1), (1, 13),
        (2, 2), (2, 12),
        (3, 3), (3, 11),
        (4, 4), (4, 10),
        (7, 7),
        (10, 4), (10, 10),
        (11, 3), (11, 11),
        (12, 2), (12, 12),
        (13, 1), (13, 13),
    ),
        (2, 'w')
    ),
    ((  # Multiplier x3 for words
        (0, 0), (0, 7), (0, 14),
        (7, 0), (7, 14),
        (14, 0), (14, 7), (14, 14),
    ),
        (3, 'w')
    ),
)


class Board:
    def __init__(self):
        self.spots = self.set_spots()
        self.spots_orig = None
        self.first = False

    def set_spots(self):
        return [[Spot(*self.multiplier(x, y))
                for y in range(15)] for x in range(15)]

    def multiplier(self, x, y):
        mult = (0, 'c')

        for set_mult in BOARD_MULT:
            if (x, y) in set_mult[0]:
                return set_mult[1]

        return mult

    def get_board(self):
        board_str = ''
        for row in self.spots:
            board_str += '- - ' * len(row) + '-\n'
            board_str += '|' + '|'.join([f'{spot.get_spot()}' for spot in row]) + '|\n'
        board_str += '- - ' * len(self.spots[0]) + '-'

        return board_str

    def revert_board(self):
        self.spots = self.spots_orig

    # def place_word(self, word, row, col, direction, hand):
    #     self.spots_orig = deepcopy(self.spots)
    #     if self.first and self.can_place_first_word(word, row, col, direction):
    #         self.place_letters(word, row, col, direction, range(len(word)))
    #         self.first = False
    #     else:
    #         spot_list = self.get_spots_to_place_word(word, row, col, direction)
    #         existing_tiles = self.tiles_in_board(spot_list)
    #         if self.can_place_word(word, existing_tiles):
    #             remain_tiles = self.tiles_diff(word, existing_tiles)
    #             unzipped_remain_tiles = zip(*remain_tiles)
    #             unzipped_list = list(unzipped_remain_tiles)
    #             if all(
    #                 [item in [tile.letter for tile in hand]
    #                     for item in unzipped_list[1]]
    #             ):
    #                 self.place_letters(
    #                     word, row, col, direction, unzipped_list[0]
    #                 )

    def can_place_first_word(self, word, row, col, direction):
        return (
            (direction and row == 7 and col <= 7 <= col+len(word)) or
            (not direction and col == 7 and row <= 7 <= row+len(word))
        )

    def tiles_in_board(self, spots):
        return [(i, s.tile.letter) for i, s in enumerate(spots) if s.tile]

    def can_place_word(self, word, tiles_in_board):
        l_word = len(word)
        l_tiles_in_board = len(tiles_in_board)
        if l_tiles_in_board == l_word or l_tiles_in_board == 0:
            return False
        else:
            return all([(word[i[0]] == i[1]) for i in tiles_in_board])

    def place_letters(self, word, row, col, direction, indexes):
        for i in indexes:
            if direction:
                self.spots[row][col+i].set_tile(word[i])
            else:
                self.spots[row+i][col].set_tile(word[i])

    def word_to_tile(self, word):
        return [Tile(letter) for letter in word]

    def get_spots_to_place_word(self, len_word, row, col, direction):
        return (
            self.spots[row][col:col+len_word]
            if direction
            else [self.spots[row+i][col] for i in range(len_word)]
        )

    def tiles_diff(self, word, letters_in_board):
        letters = list(enumerate(word))
        return [i for i in letters if i not in letters_in_board]
