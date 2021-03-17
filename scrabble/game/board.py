from .spot import Spot


class Board:
    def __init__(self):
        self.spots = self.set_spots()

    def set_spots(self):
        return [[Spot(*self.multiplier(x, y)) for y in range(15)] for x in range(15)]
        
    def multiplier(self, x, y):
        mult = (0, 'c')

        board_mult = (
            ((  # Multiplier x2 for letters 
                (0,3), (0,11),
                (2,6), (2,8),
                (3,0), (3,7), (3,14),
                (6,2), (6,6), (6,8), (6,12),
                (7,3), (7,11), 
                (8,2), (8,6), (8,8), (8,12),
                (11,0), (11,7), (11,14),
                (12,6), (12,8),
                (14,3), (14,11),
            ),
                (2,'l'),
            ),
            ((  # Multiplier x3 for letters 
                (1,5),(1,9),
                (5,1), (5,5), (5,9), (5,13),
                (9,1), (9,5), (9,9), (9,13),
                (13,5),(13,9),
            ),
                (3,'l')
            ),
            ((  # Multiplier x2 for words 
                (1,1), (1,13),
                (2,2), (2,12),
                (3,3), (3,11),
                (4,4), (4,10),
                (7,7),
                (10,4), (10,10),
                (11,3), (11,11),
                (12,2), (12,12),
                (13,1), (13,13),
            ),
                (2,'w')
            ),
            ((  # Multiplier x3 for words 
                (0,0), (0,7), (0,14),
                (7,0), (7,14),
                (14,0), (14,7), (14,14),
            ),
                (3,'w')
            ),
        )

        for set_mult in board_mult:
            for value in set_mult[0]:
                if (x,y) == value:
                    return set_mult[1]


        return mult
