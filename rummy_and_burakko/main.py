from Juegos import player
from Juegos import board
from Juegos import game


if __name__ == "__main__":
    n = ask_n_players()
    select_turn()
    new_game = Game(n)
    create_pieces()
    create_new_players(n)
    deal(remaining_pieces) 

    while(end_game == False)
        show_board() and show_hand()
        while(end_turn == False)
            show_moves()
            end_turn = ask_end_turn()
            valid_moves()
            end_game = ask_end_game()
            change_player()
    print(‘GAME OVER’)