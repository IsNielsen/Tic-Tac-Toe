#Isaac Nielsen CS1440 assn1

"""
##   code that prints pretty output and takes useer input
*    ONLY module in the project where `input()` function is called
*    Most (but not all) functions that call `print()`
*    functions returning strings with terminal escape sequences belong here
"""
from util import *
from time import sleep


def get_human_move(board, letter):
    """
    Ask a human which move to take, or whether they want to quit.
    Perform rudimentary input validation, repeating the prompt until a valid
    input is given:
     * Integers must be in the range of [1..9] (whether it represents a legal
       move is to be handled by the caller)
     * Strings beginning with 'Q' or 'q' quit the game

    Return an integer [1..9] to indicate the move to take, or False to quit the game
    """
    while True:
        show(board)
        choice = input("Place your '{}' (or 'Q' to quit)> ".format(color(letter)))
        if not choice.isdigit():
            if choice.lower().startswith('q'):
                return False
            else:
                print("I don't understand '{}', try again!\n".format(choice))
        else:
            choice = int(choice)
            if not 0 < choice < 10:
                print("Numbers must be between 1 and 9, try again!\n")
            else:
                return choice

def player_select():
    while True:
        print("0)", red("X"), green("CPU  "), "vs.", cyan("O"), green("CPU"))
        print("1)", red("X"), white("Human"), "vs.", cyan("O"), green("CPU"))
        print("2)", red("X"), green("CPU  "), "vs.", cyan("O"), white("Human"))
        print("3)", red("X"), white("Human"), "vs.", cyan("O"), white("Human"))
        p = input("Choose game mode [0-3] or Q to quit > ")
        if p == "0" or p == "1" or p == "2" or p == "3":
            return int(p)
        elif p.lower() == "joshua":
            return 4
        elif p.lower().startswith('q'):
            return p
        else:
            print("\nInvalid selection!\n")

def logo():
    """Display the game's colorful logo"""
    print()
    print(red('888888888               '), white('888888888                '), cyan('888888888                 '))
    print(red('"8888888" ooooo  ooooo  '), white('"8888888" ooo     ooooo  '), cyan('"8888888"  ooo    ooooo   '))
    print(red('   888     888  88   8  '), white('   888    888    88   8  '), cyan('   888   88   88  8       '))
    print(red('   888     888  88      '), white('   888   8ooo8   88      '), cyan('   888   88   88  8ooooo  '))
    print(red('   888     888  88    88'), white('   888  888  888 88    88'), cyan('   888   88o  88 o88      '))
    print(red('   888    88888  888888"'), white('   888  888  888  888888"'), cyan('   888   "888888 888888888'))
    print("                                                            ", "by ", yellow("DuckieCorp"), "(tm)", sep='')
    print(green("\nWOULD YOU LIKE TO PLAY A GAME?\n"))


def show(board):
    """
    Display the Tic-Tac-Toe board on the screen, in color

    When the optional parameter 'clear' is True, clear the screen before printing the board
    """
    if board:
        print(" {} | {} | {}\n---+---+---\n {} | {} | {}\n---+---+---\n {} | {} | {}\n".format(
            color(board[0][0]), color(board[0][1]), color(board[0][2]),
            color(board[0][3]), color(board[0][4]), color(board[0][5]),
            color(board[0][6]), color(board[0][7]), color(board[0][8])))



def keep_playing(board):
    """
    Accepts a board or False as input
           board: take another turn
           False: the user has requested to quit the game
    Return False if the game is over for any reason (quitting, win, lose or draw),
           or a new board to keep playing
    """
    if not board:
        return False
    who = winner(board)
    if who == "X":
        print(red("\n{} is the winner!\n".format(who)))
        return False
    elif who == "O":
        print(cyan("\n{} is the winner!\n".format(who)))
        return False
    elif full(board):
        print(green("\nStalemate.\n"))
        return False
    else:
        return board

def human_turn(board, letter):
    """
    Return False if the game is over,
           True to keep playing
    """
    while True:
        choice = get_human_move(board, letter)
        if choice is False:
            return False
        new_board = place(board, choice, letter)
        if not new_board:
            if letter == 'X':
                print(red("You can't play at {}!".format(choice)))
            else:
                print(cyan("You can't play at {}!".format(choice)))
        else:
            return new_board

def place(board, position, player):
    """
    Accepts: a game board (tuple), position (integer), and a player's identity ("X" or "O")
    Return a copy of the board with that player's mark put into the requested
    position, iff a player's mark isn't already present there.

    Otherwise, return False
    """
    if not 1 <= position <= 9:
        # player requested an out-of-bounds position
        return False

    # convert position into (row, col) coordinates
    ##row, col = pos_to_rowcol(position)

    if board[0][position-1] != 'X' and board[0][position-1] != 'O':
        # construct a brand new board
        new = []
        for element in board[0]:
            # this puts it into one dimension instead of 2
            new.append(element)
        # looks at position of 1D list
        new[position-1] = player
        # Always maintain the board as a tuple to guarantee that it
        # can never be accidentally modified
        return tuple([new])

    # if board[row][col] != 'X' and board[row][col] != 'O':
    #     # construct a brand new board
    #     new = []
    #     for r in board:
    #         new.append(list(r))
    #     new[row][col] = player
    #     # Always maintain the board as a tuple to guarantee that it
    #     # can never be accidentally modified
    #     return tuple([tuple(new[0]), tuple(new[1]), tuple(new[2])])
    # else:
    #     return False