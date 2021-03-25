from .board import Board
from .tile_bag import TileBag
from .player import Player


class Game:

    def __init__(self, name_players):
        if len(name_players) not in range(1, 5):
            raise Exception
        self.players = self.create_player(name_players)
        self.board = Board()
        self.tile_bag = TileBag()
        self.first = 0
        self.skipped_turns = 0
        self.lost_turns = []
        self.current_player = 0
        self.winner = None
        self.is_playing = True

    def create_player(self, name_players):
        return [Player(j, name) for j, name in enumerate(name_players)]

    # def first_player(self):
    #     ref = []
    #     for player in self.players:
    #         print("first call", len(self.tile_bag.tiles))
    #         player.one_draw(self.tile_bag)
    #         print("second call", len(self.tile_bag.tiles))
    #         value = player.tiles_in_hand[0].order
    #         ref.append((value))
    #     return ref.index(min(ref))

    def print_board(self):
        return self.board.get_board()

    def change_player_tiles(self, tile_amount):
        self.players.get(self.current_player).put_t_draw_t(tile_amount)

    def place_word(x, y, horizontal, word):
        self.board.place_word(word, y, x, horizontal)

    @property
    def player_count(self):
        return len(self.players)

    def resolve_challenge(self, result, player):
        if result:
            self.lost_turns.append(player)
        else:
            # Revert board
            pass

    def get_current_player_hand(self):
        curr_player = self.players[self.current_player]
        return f'{curr_player.name}:\n{curr_player.get_hand()}'

    def change_turn(self):
        self.current_player = (self.current_player + 1) % self.player_count
        if self.current_player in self.lost_turns:
            self.lost_turns.remove(self.current_player)
            self.change_turn()

    def skip_turn(self):
        self.skipped_turns += 1
        if self.skipped_turns < self.player_count * 2:
            self.change_turn()
        else:
            self.game_over()

    def game_over(self):
        self.is_playing = False
        tie = False
        winner = None
        highest = float('-inf')
        player_scores = sorted(self.count_points(True), key=lambda x: x[1])
        for player, score in enumerate(player_scores):
            if score > highest:
                highest = score
                winner = player
            tie = score == highest if not tie else True
        if tie:
            highest = float('-inf')
            player_scores = sorted(self.count_points(False), key=lambda x: x[1])
            for player, score in enumerate(player_scores):
                if score > highest:
                    highest = score
                    winner = player
        self.winner = winner

    def count_points(self, with_remaining_tiles=True):
        if with_remaining_tiles:
            scores = [
                (index, player.score - sum([
                    tile.score for tile in player.tiles_in_hand
                ])) for index, player in enumerate(self.players)
            ]
        else:
            scores = [
                (index, player.score)
                for index, player in enumerate(self.players)
            ]

        return scores

    def get_game_results(self):
        return 'Final scores:\n' + '\n'.join([
            f'{pos}: {player.name} - {player.score}'
            for pos, player in enumerate(self.players)
        ])