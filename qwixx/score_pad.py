from .row import Row


class ScorePad:
    def __init__(self):
        self.rows = self.create_rows()
        self.penalty = 0

    def create_rows(self):
        return (
                {
                    color: Row(color)
                    for color in ['red', 'yellow', 'blue', 'green']
                }
            )

    def add_penalty(self):
        self.penalty += 1
        if self.penalty < 4:
            return self.penalty
        else:
            return True  # terminar juego

    def calculate_marks(self):
        dict_marks = {
            1: 1,
            2: 3,
            3: 6,
            4: 10,
            5: 15,
            6: 21,
            7: 28,
            8: 36,
            9: 45,
            10: 55,
            11: 66,
            12: 78,
        }
        score = 0
        for _, i in self.rows.items():
            m = len(i.marks)
            subt = dict_marks[m]
            score += subt
        return score

    def calculate_score(self):
        score = self.calculate_marks()
        penalty = self.penalty * 5
        return score - penalty

    def mark_number_in_row(self, number, color):
        self.rows[color].set_mark(number)
