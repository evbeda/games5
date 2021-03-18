from .score_pad import ScorePad


class Player:
    def __init__(self):
        # self.board = []  # [row1, ro2, row3, row4]
        # self.name = name
        self.score_pad = ScorePad()

    def mark_number(self, number, color):
        self.score_pad.mark_number_in_row(number, color)

    def pass_turn(self):
        return self.score_pad.add_penalty()
