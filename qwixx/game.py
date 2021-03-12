import player


class Game:
    def __init__(self):
        self.current_player = player.Player()

    def create_dice_set(self):
        raise NotImplementedError

    def remove_die(self):
        raise NotImplementedError
