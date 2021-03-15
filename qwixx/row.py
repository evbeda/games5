class Row:
    def __init__(self, values, color):
        self.row = values
        self.color = color
        self.state = False
        self.mark = 0

    def lock_Row(self):
        self.state = True
        return True
