from .score_pad import ScorePad


class Player:
    def __init__(self):
        # self.board = []  # [row1, ro2, row3, row4]
        # self.name = name
        self.score_pad = ScorePad()

    def mark_number(self, number, color):
        for row in self.score_pad.rows:
            if row.color != color:
                continue
            row.set_marks(number)
            break

    def pass_turn(self):
        return self.score_pad.add_penalty()
