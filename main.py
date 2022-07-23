import random
import time
import sys
from playsound import playsound  # for sound effects
import ben  # add additional modules
import copy

# initialize gameboard:
numRows = 6
numColumns = 7
gb = [[' ' for i in range(numColumns)] for j in range(numRows)]
blank_spots = 42


# MAIN CODE STARTS LINE 131
# FUNCTION TO DISPLAY CURRENT BOARD:
def user_move(gb1, user_marker, opp_marker):
    valid_entry = False
    open_spot_check = False

    while valid_entry == False or open_spot_check == False:
        user_choice = input('Which column would you like to place a marker in? ')
        print('\n')

        user_int = int(user_choice)
        if user_int == 1 or user_int == 2 or user_int == 3 or user_int == 4 or user_int == 5 or user_int == 6 or user_int == 7:
            valid_entry = True
            if gb[0][user_int - 1] == ' ':
                open_spot_check = True

        if valid_entry == False or open_spot_check == False:
            print('Invalid option, please try again')

    return user_int

def print_board():
    print(' (1) (2) (3) (4) (5) (6) (7)')
    for x in range(6):
        print('-----------------------------')
        print(f'| {gb[x][0]} | {gb[x][1]} | {gb[x][2]} | {gb[x][3]} | {gb[x][4]} | {gb[x][5]} | {gb[x][6]} |')
    print('-----------------------------')


# FUNCTION TO PLACE A PIECE ON BOARD:
def place_piece(column_num, color, this_gb=gb):
    global blank_spots
    array_col = column_num - 1
    already_played = False

    for x in range(1, 6):
        if this_gb[x][array_col] != ' ' and already_played == False:
            this_gb[x - 1][array_col] = color
            already_played = True

    if already_played == False:
        this_gb[5][array_col] = color

    print_board()
    print('\n')
    blank_spots -= 1


def make_move(player_color, opponent_color, main_funct_name):
    gb_copy = copy.deepcopy(gb)
    col_choice = main_funct_name(gb_copy, player_color, opponent_color)
    return col_choice


def check_for_win(marker):
    global game_finished

    # Horizontal Wins:4
    for x in range(6):
        if gb[x][0] == gb[x][1] == gb[x][2] == gb[x][3] == marker:
            game_finished = True
        if gb[x][1] == gb[x][2] == gb[x][3] == gb[x][4] == marker:
            game_finished = True
        if gb[x][2] == gb[x][3] == gb[x][4] == gb[x][5] == marker:
            game_finished = True
        if gb[x][3] == gb[x][4] == gb[x][5] == gb[x][6] == marker:
            game_finished = True

    # Vertical Wins:
    for y in range(7):
        if gb[0][y] == gb[1][y] == gb[2][y] == gb[3][y] == marker:
            game_finished = True
        if gb[1][y] == gb[2][y] == gb[3][y] == gb[4][y] and gb[1][y] == marker:
            game_finished = True
        if gb[2][y] == gb[3][y] == gb[4][y] == gb[5][y] and gb[2][y] == marker:
            game_finished = True

    # Up Left to Right Diagonal Wins:
    for y in range(4):
        for x in range(3, 6):
            if gb[x][y] == gb[x - 1][y + 1] == gb[x - 2][y + 2] == gb[x - 3][y + 3] == marker:
                game_finished = True

    # Up Right to Left Diagonal Wins:
    for y in range(3, 7):
        for x in range(3, 6):
            if gb[x][y] == gb[x - 1][y - 1] == gb[x - 2][y - 2] == gb[x - 3][y - 3] == marker:
                game_finished = True

    # Down Left to Right Diagonal Wins:
    for y in range(4):
        for x in range(3):
            if gb[x][y] == gb[x + 1][y + 1] == gb[x + 2][y + 2] == gb[x + 3][y + 3] == marker:
                game_finished = True

    # Down Right to Left Diagonal Wins:
    for y in range(3, 7):
        for x in range(3):
            if gb[x][y] == gb[x + 1][y - 1] == gb[x + 2][y - 2] == gb[x + 3][y - 3] == marker:
                game_finished = True

    if game_finished:
        if marker == p1[3]:
            dp(f"{p1[0]} HAS EMERGED VICTORIOUS!\n")
            time.sleep(2)
            dp(f"{p2[0]} IS THE SHAMEFUL LOSER!\n")
        if marker == p2[3]:
            dp(f"{p2[0]} HAS EMERGED VICTORIOUS!\n")
            time.sleep(2)
            dp(f"{p1[0]} IS THE SHAMEFUL LOSER!\n")
    if blank_spots == 0 and game_finished == False:
        print("Looks like you tied :/")
        game_finished = True


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


# Main Script Starts Here:

blue_marker = '\033[34m◍\033[0m'
red_marker = '\033[31m◍\033[0m'

# EACH USER MAKE A LIST - that contains their name, bot name, & function name -  WITH THIS FORMAT:
# ["Player Name", "BOT NAME", player_function (or module.function)
# example:
ben_list = ["BEN", "JAMES THE DESTROYER", ben.main]
adam_list2 = ["ADAM", "BOB THE BUILDER", user_move]

# replace with whatever players are competing
player_a = ben_list
player_b = adam_list2

game_finished = False
first_turn = random.randint(0, 1)

dp = delay_print
# introduction sequence

# music
playsound("background.wav", False)

dp("WELCOME TO THE CONNECT4 BATTLE ARENA!\n")
print()
time.sleep(1)
dp("MEET TODAY'S FIERCE CHALLENGERS:\n")
time.sleep(1)
dp(f"{player_a[1]} VS {player_b[1]}\n")
time.sleep(1)
print()
dp(f"WHO WILL WIN? THE MIGHTY {player_a[0]} OR THE FIERCE {player_b[0]}?\n")
print()
dp("I'LL FlIP A COIN TO SEE WHO GOES FIRST\n")

global p1
global p2
if first_turn == 0:
    p1 = player_a
    p2 = player_b
else:
    p1 = player_b
    p2 = player_a

time.sleep(1)
dp(f"{p1[1]} WILL GO FIRST THIS TIME!\n")
time.sleep(1)
print()
dp("MAY THE BEST BOT WIN!\n")
time.sleep(2)
print()
# players colors can be accessed using p1[3] or p2[3]
p1.append(blue_marker)
p2.append(red_marker)
print_board()


while not game_finished:
    print(f"IT'S {p1[1]}'S TURN!")
    #time.sleep(1)
    p1_choice = make_move(p1[3], p2[3], p1[2])
    print(f"I CHOOSE COLUMN {p1_choice}.")
    place_piece(p1_choice, p1[3])
    playsound("plink.wav", False)
    check_for_win(p1[3])
    time.sleep(2)

    if not game_finished:
        print(f"IT'S {p2[1]}'S TURN!")
        #time.sleep(1)
        p2_choice = make_move(p2[3], p1[3], p2[2])
        print(f"I CHOOSE COLUMN {p2_choice}.")
        place_piece(p2_choice, p2[3])
        playsound("plink.wav", False)
        check_for_win(p2[3])
        time.sleep(1)