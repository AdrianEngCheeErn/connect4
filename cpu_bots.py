import random
from gameplay import *


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    while True:
        col = random.randint(1, 7)
        if drop_piece(board, player, col) == True:
            return col


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty.
    It first checks for an immediate win and plays that move if possible.
    If no immediate win is possible, it checks for an immediate win
    for the opponent and blocks that move. If neither of these are
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    # checking for the immidiate win move for CPU player
    moves = find_win_move(board, player)
    # check if winning move was found
    if len(moves) != 0:
        drop_piece(board, player, moves[0])
        return moves[0]

    # There is no immidiate win move for CPU Player.
    # Will check immidiate win moves for opposing player to block it.
    moves = find_win_move(board, player%2 + 1)
    # check if winning move was found for opposing player
    if len(moves) != 0:
        # block the winning move for opposing player
        drop_piece(board, player, moves[0])
        return moves[0]

    # CPU could not find a good move and proceeds with random move
    return cpu_player_easy(board, player)


def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.

    Below described strategy in sequence:

    1. Check if there is winning move for the cuurent player. If yes, then do It.
    2. Check if there is winning move for opposing plater. If yes, then block it.
    3. Check if there wining move for the opposing player after the current players move.
    If yes, then append the move to the bad moves list in order to avoid it.
    4. Check if there are moves which can lead to the winning of opposing player in two moves.
    If yes, then append the move to blocking moves list
    5. Check if there are moves which can lead to the winning of current player in two moves.
    If yes, then append the move to posible winning moves list
    6. If there was no immidate winning moves for the current player and opposing player then make
    following moves in order of availibility
        a. Make a blocking move but avoid bad moves
        b. Make a potential/posible winning move but avoid bad list_bad_moves
        c. Check which moves are availble: meaning that they are not bad and the column is not full.
        Make the random move to the available column

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """

    # Implement your solution below
    # List of moves current player MUST NOT do
    list_bad_moves = []
    # List of moves available for current player
    list_available_moves = []
    # List of moves which could potentially lead to opposing player winning in 2 moves
    list_blocking_moves = []
    # List of moves which could lead to current player winning in 2 moves
    list_possible_winning_moves = []

    # checking for the immidiate win moves for current player
    moves = find_win_move(board, player)
    # check if winning move was found for current player
    if len(moves) != 0:
        drop_piece(board, player, moves[0])
        return moves[0]

    # There is no immidiate win move for current Player.
    # Will check immidiate win moves for opposing player to block it.
    moves = find_win_move(board, player%2 + 1)
    # check if winning move was found
    if len(moves) != 0:
        # block the opposing winning move
        drop_piece(board, player, moves[0])
        return moves[0]


    # We will go one level deeper and anylyze two moves for both players
    for col in range(7):

        # Checking if there is a bad move for current player. Meaning that it will lead to winning move for opposing player.
        # This is first move of the current player
        # Checking if the move is valid
        if drop_piece(board, player, col+1) == True:
            # checking if there wining move for the opposing player after the current player's first move
            moves = find_win_move(board, player%2 + 1)
            # undo the first move
            undo_move(board, col)
            # check if there was immidiate win moves for the opposing player after the current player's first move
            if len(moves) != 0:
                # the first move leads to the opposing player win, hence undo it
                # add the move that will lead to the lost, to the list of bad moves to avoid them
                list_bad_moves.append(col)
                # end current loop to skip this bad move and continue to the next iteration
                continue


        # checking if that current player have two consequent move that could lead to win
        # doing the first move for the CPU player
        if drop_piece(board, player, col+1) == True:
            # checking if the first move can lead to the second winning moves
            moves = find_win_move(board, player)
            # undo the first move for the current player
            undo_move(board, col)
            # check if second move that can lead to win was found
            if len(moves) > 1:
                drop_piece(board, player, col+1)
                return col + 1 
            elif len(moves) == 1:
                list_possible_winning_moves.append(col)


        # Will go one level deeper to check if there is winning position in two moves for opposing player
        # checking if the move is valid
        if drop_piece(board, player%2 + 1, col+1) == True:
            # checking if there is second move that willl lead to win for the opposing player
            moves = find_win_move(board, player%2 + 1)
            # undo the first move for the opposing player
            undo_move(board, col)
            # check if the first move of opposing player can lead to 100% lost for the first CPU user
            if len(moves) > 1:
                # block the first move for opposing player that can lead to 100% second winning move
                drop_piece(board, player, col+1)
                return col + 1
            elif len(moves) == 1:
                list_blocking_moves.append(col)


    # blocking moves that can lead to the opposing player win
    if len(list_blocking_moves) > 0:
        move = random.choice(list_blocking_moves)
        drop_piece(board, player, move+1)
        return move+1

    # moves that can lead to the current player in two moves
    if len(list_possible_winning_moves) > 0:
        move = random.choice(list_possible_winning_moves)
        drop_piece(board, player, move+1)
        if find_win_move(board, player%2 + 1) == 0:
            return move+1
        undo_move(board, col)

    # Try to make a move in the middle columns, e.g avoiding the first and last column
    for col in range(1, 5):
        if drop_piece(board, player, col + 1) == True:
            if col not in list_bad_moves:
                return col+1

    # trying to make a move to first or last columns
    for col in [0,6]:
        if col not in list_bad_moves:
            if drop_piece(board, player, col + 1) == True:
                return col+1

    # only bad moves left
    move = random.choice(list_bad_moves)
    drop_piece(board, player, move+1)
    return move+1