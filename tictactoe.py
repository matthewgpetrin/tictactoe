import time
import random
import keyboard

#How to play:
# Execute the script
# Use the arrow keys to move
# Press space to claim a box

# Explanation:
# Upon running script, the game board will be printed out in the terminal. At 
# any given time, variables track the current player, game state, and board 
# state as well as the row and column the current player is hovering over. When 
# the script is run, the board is initialized with all spaces empty. Current 
# row and column are set to 1, game over is set to False, stalemate is set to 
# False, and the player variable is randomly selected from EX and OH. Once play
# has begun, the current player may move between spaces using the arrow keys. 
# This behavior is handled using a keyboard module hook. The board is reprinted 
# every 0.4 seconds, and the box being selected with be highlighted. When a 
# player makes a legal move, the game state will be updated. If the game is not 
# over, the player variable switches and play continues. If an illegal move is 
# attempted, nothing will happen.

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

# Column and row currently being highlighted
current_row = 1
current_col = 1

# Header and footer text to be displayed
header = "   TIC TAC TOE   "
footer = "     WELCOME     "

# Keyboard logic executes on hook call
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

# Hook executes on key press
keyboard.hook(on_press)

# Clear lines for new frame
def clear_lines(lines):
    for i in range(lines):
        print("\033[1A", end="\r")

# Print the spaces on the game board. Color the current space
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

# Print header box and text
def print_header(color, delay):
    print("p-----------------q")
    time.sleep(delay)
    print("|" + color + header + RESET + "|")
    time.sleep(delay)
    print("b-----------------d")
    time.sleep(delay)

# Print footer box and text
def print_footer(color, delay):
    print("p-----------------q")
    time.sleep(delay)
    print("|" + color + footer + RESET + "|")
    time.sleep(delay)
    print("b-----------------d")
    time.sleep(delay)

# Print and clear header, spaces, and footer a specified number of times
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

# Move up
def move_U():
    global current_row
    if current_row > 0:
        current_row = current_row - 1

# Move down
def move_D():
    global current_row
    if current_row < 2:
        current_row = current_row + 1

# Move left
def move_L():
    global current_col
    if current_col > 0:
        current_col = current_col - 1

# Move right
def move_R():
    global current_col
    if current_col < 2:
        current_col = current_col + 1

# Switch current player
def swap_players():
    global player
    if player == EX:
        player = OH
    elif player == OH:
        player = EX

# Check for stalemate conditions
def is_stalemate():
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if board[r][c] == EMPTY:
                return 0
    return 1

# Check for win conditions
def is_game_over():
    global winner
    
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

# Execute on space bar press. Make play, check for win and stalemate
def on_play():
    global game_over
    global stalemate

    global header
    global footer

    if board[current_row][current_col] != EMPTY:
        pass
    else:
        board[current_row][current_col] = player
        if is_game_over(): 
            game_over = True
            header = "    GAME OVER    "
            footer = "  PLAYER " + winner + " WINS  "
        elif is_stalemate():
            game_over = True
            stalemate = True
            header = "    GAME OVER    "
            footer = "    STALEMATE    "
        else:
            swap_players()
            footer = " PLAYER " + player + "'s TURN "
            
# Execute on game start. Prints board and randomized starting player          
def on_start():
    global player
    global footer
    player = random.choice(list((EX, OH)))
    
    footer = "     WELCOME     "
    print_header(RESET, 0.05)
    print_spaces(RESET, RESET, 0.05)
    print_footer(RESET, 0.05)
    
    blink_game(COLOR, 0.2, 5)
    
    footer = " PLAYER " + player + "'s TURN "
    clear_lines(11)
    print_header(RESET, 0)
    print_spaces(RESET, RESET, 0)
    print_footer(RESET, 0)


# MAIN GAME LOOP
on_start()

# Print and clear board every 0.4 seconds
while game_over == False:
    clear_lines(8)
    print_spaces(RESET, RESET, 0)
    print_footer(RESET, 0)

    time.sleep(0.4)

    clear_lines(8)
    print_spaces(COLOR, "\033[31;1;4m", 0)
    print_footer(RESET, 0)
    
    time.sleep(0.4)

blink_game(COLOR, 0.2, 5) 