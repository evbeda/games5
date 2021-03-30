class NotCanmark(Exception):
    pass


class Row:
    blocked_rows = []

    def __init__(self, color):
        self.color = color
        self.numbers = self.create_row_numbers()
        self.marks = []

    def create_row_numbers(self):
        return (
            tuple(range(2, 13))
            if self.color in ['red', 'yellow']
            else tuple(reversed(range(2, 13)))
        )

    def lock_Row(self):
        self.blocked_rows.append(self.color)

    @property
    def is_locked(self):
        if self.color in self.blocked_rows:
            return True

    def can_mark_last(self):
        return len(self.marks) >= 5

    def set_mark(self, number):
        if self.check_row_lock(number):
            return self.marks.append(number)

    def check_row_lock(self, number):
        if (
            (self.is_locked is None)
            and (number not in self.marks)
        ):
            return self.can_mark(number)
        else:
            False

    def calculate_marks(self):
        set_marks = (
            (1, 1),
            (2, 3),
            (3, 6),
            (4, 10),
            (5, 15),
            (6, 21),
            (7, 28),
            (8, 36),
            (9, 45),
            (10, 55),
            (11, 66),
            (12, 70),
        )
        for mark in set_marks:
            if len(self.marks) == mark[0]:
                return mark[1]

    def can_mark(self, number):
        return(
            self.marks == []
        ) or (
            (
                number > self.marks[-1]
            ) and (
                self.color in ['red', 'yellow']
            )
        ) or (
            (
                number < self.marks[-1]
            ) and (
                self.color in ['blue', 'green']
            )
        )
