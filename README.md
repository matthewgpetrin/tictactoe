# Console-Based Tic-Tac-Toe
## Overview:
This project is a console-based approach to a basic tic-tac-toe game. The game board will be displayed in the local terminal. Users may make plays using the keyboard.

Note: because this game is console-based, some behaviors may vary depending on the specific terminal. PyCharm's terminal, for example, will not work properly, or may display different colors than expected.

## How To Play:
- Execute ```python.exe tictactoe.py```
- Use the arrow keys to move
- Press the space bar to claim a box  

## Functions:
### **on_press(event)**
Is executed when keyboard input is supplied. Calls the ```move_X()``` and ```on_play()``` functions based on ```event```.
### **clear_lines(lines)**
 Accepts 1 int. Moves cursor back ```lines``` number of lines. Does not actually wipe the data contained on each one.
 ### **print_spaces(color_empty, color_taken, delay**)
 Accepts 2 ANSI escape sequences and a float. Writes 5 lines to terminal with ```delay``` seconds between each one. The first and last contain the game border. The middle 3 contain brackets (denoting spaces) and their corresponding values. ```EMPTY``` spaces will be colored ```color_empty``` and non empty spaces will be colored ```color_taken```.
 ### **print_header(color, delay)**
 Accepts 1 ANSI escape sequence and a float. Prints 3 lines to console. The first and last are borders. The middle is the header message with color ```color```
 ### **print_footer(color, delay)**
 Accepts 1 ANSI escape sequence and a float. Prints 3 lines to console. The first and last are borders. The middle is the footer message with color ```color```
 ### **blink_game(color, delay, count)**
 Accepts 1 ANSI escape sequence, 1 float, and 1 int. Prints the header, spaces, and footer to the terminal switching between color ```color``` and the default color ```count``` number of times with ```delay``` seconds between each flash.
 ### **move_U():**
 Moves the cursor up one space.
 ### **move_D():**
 Moves the cursor down one space.
 ### **move_L():**
 Moves the cursor left one space.
 ### **move_R():**
 Moves the cursor right one space.
 ### **swap_players()**
 Switches ```player``` from ```EX``` to ```OH``` and vice versa
 ### **is_stalemate()**
 Checks to see if any spaces remain empty and returns ```True``` or ```False```. Should only be called after ```is_game_over()```.
 ### **is_game_over()**
 Checks all possible win conditions and returns ```True``` or ```False```.
 ## **on_play()**
 Called when player presses space. First checks if spot is ```EMPTY```. If the current spot is ```EMPTY```, its value is changed to ```player```. ```is_game_over()``` and ```is_stalemate()``` are called and ```game_over``` and ```stalemate``` are updated accordingly. If neither returns ```True``` nor ```False```, ```swap_player()``` is called and play continues.