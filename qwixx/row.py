class Row:
    def __init__(self, color):
        self.color = color
        self.numbers = self.create_row_numbers()
        self.is_locked = False
        self.marks = []

    def create_row_numbers(self):
        return (
                tuple(range(2, 13))
                if self.color in ['red', 'yellow']
                else tuple(reversed(range(2, 13)))
            )

    def lock_Row(self):
        self.is_locked = True
        return True

    def can_mark_last(self):
        return len(self.marks) >= 5

    def set_mark(self, number):
        if self.check_row_lock(number):
            self.marks.append(number)

    def check_row_lock(self, number):
        if (
            (not self.is_locked)
            and (number not in self.marks)
        ):
            return self.can_mark(number)
        else:
            return False

    def can_mark(self, number):
        return(
            (number > self.marks[-1])
            and (self.color in ['red', 'yellow'])
        ) or (
            (number < self.marks[-1])
            and (self.color in ['blue', 'green'])
        )
