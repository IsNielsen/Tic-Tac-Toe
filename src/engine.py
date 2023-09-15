#Isaac Nielsen CS1440 assn1

"""
##   this module is for functions that drive the main game loop
*    4 different game loops
*    controls how players take turns
*    functions here MAY output messages with help from other functions in interface.py
"""
from interface import *
CPU_DELAY = 0.75
def cpu_vs_cpu(strategy_x, strategy_o):
    """Game mode 0: run the game between two CPU opponents"""
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', strategy_x)
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', strategy_o)
        if not keep_playing(board):
            break
    show(board)

def cpu_vs_human(cpu_strategy):
    board = make_board()
    while True:
        show(board)
        board = cpu_turn(board, 'X', cpu_strategy)
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)

def human_vs_human():
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        board = human_turn(board, 'O')
        if not keep_playing(board):
            break
    show(board)

def human_vs_cpu(cpu_strategy):
    board = make_board()
    while True:
        board = human_turn(board, 'X')
        if not keep_playing(board):
            break
        show(board)
        board = cpu_turn(board, 'O', cpu_strategy)
        if not keep_playing(board):
            break
    show(board)

def game(strategy_x, strategy_o):
    global CPU_DELAY
    clear()
    print(green("GREETINGS PROFESSOR FALKEN\n"))
    sleep(CPU_DELAY)
    print(green("SHALL WE PLAY A GAME?\n"))
    sleep(CPU_DELAY * 2)
    orig_delay = CPU_DELAY
    clear()
    for _ in range(40):
        board = make_board()
        clear()
        while True:
            if CPU_DELAY > 0.025:
                CPU_DELAY *= 0.95
            home()
            show(board)
            board = cpu_turn(board, 'X', strategy_x, verbose=False)
            if not keep_playing(board):
                break
            home()
            show(board)
            board = cpu_turn(board, 'O', strategy_o, verbose=False)
            if not keep_playing(board):
                break
        clear()
        show(board)
        keep_playing(board)
        sleep(CPU_DELAY)
    CPU_DELAY = orig_delay
    sleep(CPU_DELAY)
    print(green("A STRANGE GAME.\n"))
    sleep(CPU_DELAY * 2)
    print(green("THE ONLY WINNING MOVE IS NOT TO PLAY.\n"))
    sleep(CPU_DELAY * 2)
    print(green("HOW ABOUT A NICE GAME OF CHESS?\n"))
    sleep(CPU_DELAY * 5)

def cpu_turn(board, letter, strategy, verbose=True):
    if letter == "X":
        color = red
    else:
        color = cyan
    if verbose:
        print(color("CPU {} is taking its turn...".format(letter)), end=' ', flush=True)
    sleep(CPU_DELAY)
    choice = strategy(board)+1
    if verbose:
        print(color("playing on {}\n".format(choice)))
    return place(board, choice, letter)