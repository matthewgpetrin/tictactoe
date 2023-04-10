import os
import time
import keyboard

# Time at last keyboard stroke
debounce_time = 0

# ANSI escape codes for terminal
COLOR = "\033[33m"
RESET = "\033[0m"

# Player value macros
EMPTY = " "
EX = "x"
OH = "o"

# Track current player and winner
player = EX
winner = EX 
 
# Track game state
game_over = False
stalemate = False

# Board variables
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

current_row = 1
current_col = 1

current_header = "   TIC TAC TOE   "
current_footer = "     WELCOME     "

# KEYBOARD LOGIC AND HOOK
def on_press(event):
    global debounce_time
    if time.time() - debounce_time > 0.2:
        debounce_time= time.time()
        if event.name == "space":
            on_play()
        elif event.name == "up":
            move_U()
        elif event.name == "down":
            move_D()
        elif event.name == "left":
            move_L()
        elif event.name == "right":
            move_R()

keyboard.hook(on_press)

# GAME DISPLAY FUNCTIONS
def clear_lines(lines):
    for i in range(lines):
        print("\033[1A", end="\r")


def print_spaces(color_empty, color_taken, delay):
    print("|                 |")
    time.sleep(delay)

    for r, row in enumerate(board):
        print("|    ", end="")
        for c, col in enumerate(row):
            if r == current_row and c == current_col:
                if board[r][c] == EMPTY:
                    print(color_empty + "[" + RESET + board[r][c] + color_empty + "]", end=RESET)
                else:
                    print(color_taken + "[" + RESET + board[r][c] + color_taken + "]", end=RESET)    
            else:
                print("[" + board[r][c] + "]", end="")
        print("    |")
        time.sleep(delay)

    print("|                 |")
    time.sleep(delay)


def print_header(color, delay):
    print("p-----------------q")
    time.sleep(delay)
    print("|" + color + current_header + RESET + "|")
    time.sleep(delay)
    print("b-----------------d")
    time.sleep(delay)


def print_footer(color, delay):
    print("p-----------------q")
    time.sleep(delay)
    print("|" + color + current_footer + RESET + "|")
    time.sleep(delay)
    print("b-----------------d")
    time.sleep(delay)


def blink_game(color, delay, count):
    for i in range(count):
        clear_lines(11)

        print_header(RESET, 0)
        print_spaces(RESET, RESET, 0)
        print_footer(RESET, 0)

        time.sleep(delay)
        clear_lines(11)
   
        print_header(COLOR, 0)
        print_spaces(RESET, RESET, 0)
        print_footer(COLOR, 0)

        time.sleep(delay)

# MOVEMENT FUNCTIONS
def move_U():
    global current_row
    if current_row > 0:
        current_row = current_row - 1


def move_D():
    global current_row
    if current_row < 2:
        current_row = current_row + 1


def move_L():
    global current_col
    if current_col > 0:
        current_col = current_col - 1


def move_R():
    global current_col
    if current_col < 2:
        current_col = current_col + 1

# GAME LOGIC
def swap_players():
    global player
    if player == EX:
        player = OH
    elif player == OH:
        player = EX


def is_stalemate():
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == EMPTY:
                return 0
    return 1


def is_game_over():
    for i, row in enumerate(board):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            winner = player
            return 1

    for j, col in enumerate(board):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            winner = player
            return 1

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        winner = player
        return 1

    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        winner = player
        return 1

    return 0


def on_play():
    global game_over
    global stalemate

    global current_header
    global current_footer

    if board[current_row][current_col] != EMPTY:
        pass
    else:
        board[current_row][current_col] = player
        if is_game_over(): 
            game_over = True
            current_header = "    GAME OVER    "
            current_footer = "  PLAYER " + winner + " WINS  "
        elif is_stalemate():
            game_over = True
            stalemate = True
            current_header = "    GAME OVER    "
            current_footer = "    STALEMATE    "
        else:
            swap_players()
            current_footer = " PLAYER " + player + "'s TURN "


# MAIN GAME LOOP
print_header(RESET, 0.05)
print_spaces(RESET, RESET, 0.05)
print_footer(RESET, 0.05)

blink_game(COLOR, 0.2, 5)

current_footer = " PLAYER " + player + "'s TURN "
clear_lines(11)
print_header(RESET, 0)
print_spaces(RESET, RESET, 0)
print_footer(RESET, 0)

while game_over == False:
    clear_lines(8)
    print_spaces(RESET, RESET, 0)
    print_footer(RESET, 0)

    time.sleep(.4)

    clear_lines(8)
    print_spaces(COLOR, "\033[31;1;4m", 0)
    print_footer(RESET, 0)
    
    time.sleep(.4)

blink_game(COLOR, 0.2, 5) 