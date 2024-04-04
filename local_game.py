from gameplay import *
from system import *


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    clear_screen()
    board = create_board()
    print_board(board)
    move = execute_player_turn(1, board)
    end = 0
    player = 1

    while True:
        clear_screen()
        print_board(board)
        if player == 1:
            print(f"Player 1 dropped a piece into column {move}")
            move = execute_player_turn(2, board)
            player = 2
        elif player == 2:
            print(f"Player 2 dropped a piece into column {move}")
            move = execute_player_turn(1, board)
            player = 1

        end = end_of_game(board)

        if end == 1:
            clear_screen()
            print_board(board)
            print(f"Player 1 has won the game!")
            break
        elif end == 2:
            clear_screen()
            print_board(board)
            print(f"Player 2 has won the game!")
            break
        elif end == 3:
            clear_screen()
            print_board(board)
            print("Draw! Nobody has won.")
            break