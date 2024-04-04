import os


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below
    board = []

    for _ in range(6):
            board.append([0]*7)

    return board


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    # Implement your solution below
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O")
    print("")
    print("  1   2   3   4   5   6   7", end="")
    for posY in range(6):
            print("\n --- --- --- --- --- --- ---")
            print( "|", end="")
            for posX in range(7):
                    if board[posY][posX] == 0:
                            print("   |", end= "")
                    elif board[posY][posX] == 1:
                            print(" X |", end="")
                    elif board[posY][posX] == 2:
                            print(" O |", end="")
    print("")
    print(" --- --- --- --- --- --- ---")
    print("=============================")


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')