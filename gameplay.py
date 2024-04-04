def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    # Implement your solution below
    row = 5
    while row >= 0:
        if board[row][column - 1] == 0:
            board[row][column - 1] = player
            return True
        row -= 1
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    input_as_int = int(validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5","6", "7"]))
    drop_success = drop_piece(board, player, input_as_int)
    while drop_success == False:
        print("That column is full, please try again.")
        input_as_int = int(validate_input(f"Player {player}, please enter the column you would like to drop your piece into: ", ["1", "2", "3", "4", "5", "6", "7"]))
        drop_success = drop_piece(board, player, input_as_int)
    return input_as_int


def end_of_game(board):
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # Implement your solution below
    #  horizontal line check
    for row in range(6):
        for col in range(4):
            if board[row][col] == 1 and board[row][col+1] == 1 and board[row][col+2] == 1 and board[row][col+3] == 1:
                return 1
            elif board[row][col] == 2 and board[row][col+1] == 2 and board[row][col+2] == 2 and board[row][col+3] == 2:
                return 2

    #  vertical line check
    for row in range(3):
        for col in range(7):
            if board[row][col] == 1 and board[row+1][col] == 1 and board[row+2][col] == 1 and board[row+3][col] == 1:
                return 1
            elif board[row][col] == 2 and board[row+1][col] == 2 and board[row+2][col] == 2 and board[row+3][col] == 2:
                return 2

    #  diagonal top to bottom line check
    for row in range(3):
        for col in range(4):
            if board[row][col] == 1 and board[row+1][col+1] == 1 and board[row+2][col+2] == 1 and board[row+3][col+3] == 1:
                return 1
            elif board[row][col] == 2 and board[row+1][col+1] == 2 and board[row+2][col+2] == 2 and board[row+3][col+3] == 2:
                return 2

    #  diagonal bottom to top line check
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == 1 and board[row-1][col+1] == 1 and board[row-2][col+2] == 1 and board[row-3][col+3] == 1:
                return 1
            elif board[row][col] == 2 and board[row-1][col+1] == 2 and board[row-2][col+2] == 2 and board[row-3][col+3] == 2:
                return 2

    #*** check if there are empty cells. If yes then its not end of the game
    for row in range(6):
        for col in range(7):
            if board[row][col] == 0:
                return 0

    # draw
    return 3


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below
    while True:
            user_input = input(prompt)
            if user_input in valid_inputs:
                break
    else:
            print("Invalid input, please try again.")

    return user_input


def undo_move(board, col):
    """
    Undo the last move which was done on input column.


    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :return: True if move was undone and False otherwise
    """
    # print("Initial Board")
    # print_board(board)

    # Iterates through the column passed as input to undo the move
    for row in range (6):
        if board[row][col] != 0:
            board[row][col] = 0
            return True

    return False


def find_win_move(board, player):
    """
    Find winning move if exist for the player


    :param board: The game board, 2D list of 6x7 dimensions.
    :param col: The column for which the move will be done.
    :return: the list of moves that will lead to a winning move, list.
    """
    # iterate moves for all columns
    moves = []
    for col in range(7):
        # checking if the move is valid
        if drop_piece(board, player, col+1) == True:
            # checking if the move is a win move for the player
            if end_of_game(board) == player:
                # undo winning move
                undo_move(board, col)
                # adds winning move to the list
                moves.append(col + 1)
            else:
                # if the current move is not a win move, then undo move
                undo_move(board, col)
    # returns winning moves
    return moves
