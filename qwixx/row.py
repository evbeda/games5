class Row:
    def __init__(self, color):
        self.color = color
        self.numbers = self.create_row_numbers()
        self.state = False
        self.marks = []

    def create_row_numbers(self):
        return (tuple(range(2, 13)) 
            if self.color in ['red', 'yellow']
            else tuple(reversed(range(2, 13))))

    def lock_Row(self):
        self.state = True
        return True

    def can_mark_last(self):
        return len(self.marks) >= 5

    def set_marks(self, number):
        if self.can_mark(number):
            self.marks.append(number)

    def can_mark(self, number):
        if (number > self.marks[-1]) and (self.color in ['red', 'yellow']):
            return True
        elif (number < self.marks[-1]) and (self.color in ['blue', 'green']):
            return True
        else:
            return False
