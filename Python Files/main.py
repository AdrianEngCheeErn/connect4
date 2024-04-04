from system import *
from gameplay import *
from cpu_bots import *
from local_game import *


def main():
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below
    while True:
        clear_screen()
        print("=============== Main Menu ===============")
        print("Welcome to Connect 4!")
        print("1. View Rules")
        print("2. Play a local 2 player game")
        print("3. Play a game against the computer")
        print("4. Exit")
        print("=========================================")

        menuOption = int(validate_input("Please select the menu option : ", ["1", "2", "3", "4"]))

        if menuOption == 1:
            clear_screen()
            print_rules()
        elif menuOption == 2:
            local_2_player_game()
        elif menuOption == 3:
            game_against_cpu()
        elif menuOption == 4:
            return
        input()


def game_against_cpu():
    """
    Runs a game of Connect 4 against the computer.

    :return: None
    """
    # Implement your solution below

    print("Please select CPU player level:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    level = validate_input("Please select level: ", ["1", "2", "3"])
    board = create_board()
    clear_screen()
    print_board(board)
    move = execute_player_turn(1, board)
    player = 1

    while True:
        clear_screen()
        print_board(board)
        if player == 1:
            print(f"Player {player} dropped a piece into column {move}")
            if level == "1":
                move = cpu_player_easy(board, 2)
            elif level == "2":
                move = cpu_player_medium(board, 2)
            else:
                move = cpu_player_hard(board, 2)
            #make a move for the CPU
            player = 2
        elif player == 2:
            print(f"Player CPU dropped a piece into column {move}")
            move = execute_player_turn(1, board)
            player = 1
        end = end_of_game(board)
        if end == 1 or end == 2:
            clear_screen()
            print_board(board)
            print(f"Player {player} has won the game!")
            return
        elif end == 3:
            clear_screen()
            print_board(board)
            print("Draw! Nobody has won.")
            return

if __name__ == "__main__":
    main()
