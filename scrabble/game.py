from .board import Board
from .tile_bag import TileBag
from .player import Player


class Game:

    def __init__(self, name_players):
        if len(name_players) not in range(1, 5):
            raise Exception
        self.board = Board()
        self.tile_bag = TileBag()
        self.players = self.create_player(name_players)
        self.first = 0
        self.skipped_turns = 0
        self.lost_turns = []
        self.current_player = 0
        self.game_results = []
        self.is_playing = True

    def create_player(self, name_players):
        players = []
        for j, name in enumerate(name_players):
            player = Player(j, name)
            player.full_draw(self.tile_bag)
            players.append(player)
        return players

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

    def place_word(self, x, y, direction, word):
        self.board.place_word(
            word, y, x, direction, self.players.get(self.current_player)
        )

    @property
    def player_count(self):
        return len(self.players)

    def resolve_challenge(self, result, player=None):
        if result:
            if player is not None:
                self.lost_turns.append(player)
            else:
                raise Exception
        else:
            self.board.revert_board()
            self.players[self.current_player].revert_points()

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
        self.game_results = sorted(
            self.count_points(True), key=lambda x: x[1], reverse=True
        )
        if self.game_results[0][1] == self.game_results[1][1]:
            self.game_results = sorted(
                self.count_points(False), key=lambda x: x[1], reverse=True
            )

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
            f'{pos+1}: {self.players[result[0]].name} - {result[1]}'
            for pos, result in enumerate(self.game_results)
        ])
