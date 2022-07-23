import random
import copy


def main(gb1, my_color, opponent_col):
    reset_gb = copy.deepcopy(gb1)
    blue_marker = '\033[34m◍\033[0m'
    red_marker = '\033[31m◍\033[0m'

    def print_board(gb):
        print(' (1) (2) (3) (4) (5) (6) (7)')
        for x in range(6):
            print('-----------------------------')
            print(f'| {gb[x][0]} | {gb[x][1]} | {gb[x][2]} | {gb[x][3]} | {gb[x][4]} | {gb[x][5]} | {gb[x][6]} |')
        print('-----------------------------')

    def place_piece(array_col, color):
        for x in range(1, 6):
            if gb1[x][array_col] != ' ':
                gb1[x - 1][array_col] = color
                return x - 1

        gb1[5][array_col] = color
        return 5

    def check_for_win(marker):
        game_finished = False
        # print("marker")
        # print(marker)

        # Horizontal Wins:
        for x in range(6):
            if gb1[x][0] == gb1[x][1] == gb1[x][2] == gb1[x][3] == marker:
                game_finished = True
            if gb1[x][1] == gb1[x][2] == gb1[x][3] == gb1[x][4] == marker:
                game_finished = True
            if gb1[x][2] == gb1[x][3] == gb1[x][4] == gb1[x][5] == marker:
                game_finished = True
            if gb1[x][3] == gb1[x][4] == gb1[x][5] == gb1[x][6] == marker:
                game_finished = True

        # Vertical Wins:
        for y in range(7):
            if gb1[0][y] == gb1[1][y] == gb1[2][y] == gb1[3][y] == marker:
                game_finished = True
            if gb1[1][y] == gb1[2][y] == gb1[3][y] == gb1[4][y] == marker:
                game_finished = True
            if gb1[2][y] == gb1[3][y] == gb1[4][y] == gb1[5][y] == marker:
                game_finished = True

        # Up Left to Right Diagonal Wins:
        for y in range(4):
            for x in range(3, 6):
                if gb1[x][y] == gb1[x - 1][y + 1] == gb1[x - 2][y + 2] == gb1[x - 3][y + 3] == marker:
                    game_finished = True

        # Up Right to Left Diagonal Wins:
        for y in range(3, 7):
            for x in range(3, 6):
                if gb1[x][y] == gb1[x - 1][y - 1] == gb1[x - 2][y - 2] == gb1[x - 3][y - 3] == marker:
                    game_finished = True

        # Down Left to Right Diagonal Wins:
        for y in range(4):
            for x in range(3):
                if gb1[x][y] == gb1[x + 1][y + 1] == gb1[x + 2][y + 2] == gb1[x + 3][y + 3] == marker:
                    game_finished = True

        # Down Right to Left Diagonal Wins:
        for y in range(3, 7):
            for x in range(3):
                if gb1[x][y] == gb1[x + 1][y - 1] == gb1[x + 2][y - 2] == gb1[x + 3][y - 3] == marker:
                    game_finished = True
        return game_finished

    def sort_choices(choices):
        king = choices[0]
        for each in choices:
            if king[0] < each[0]:
                king = each
            if king[0] == each[0]:
                coin_flip = random.randint(0, 1)
                if coin_flip == 1:
                    king = each
        return king[1]

    def cf(y, x):
        """converts coordinate list to nested list"""
        return gb1[y][x]

    def order_col_pref(col):
        prefs = {0: 2, 1: 4, 2: 6, 3: 10, 4: 6, 5: 4, 6: 2}
        return prefs[col]

    other_color = {blue_marker: red_marker, red_marker: blue_marker}
    opponent_col = other_color[my_color]

    move_options = []
    for x in range(7):
        score = 0
        # print(gb1)
        if cf(0, x) != " ":
            score -= 100000
        y = place_piece(x, my_color)
        # print("coord")
        # print([x, y])

        # print(check_for_win(my_color))
        if check_for_win(my_color):
            score += 1000
        score += order_col_pref(x)
        if x in [1, 2, 3, 4, 5]:
            if cf(y, x - 1) == my_color or cf(y, x + 1) == my_color:
                score += 20
        if x in [2, 3, 4]:
            if cf(y, x - 1) == my_color and cf(y, x - 2) == my_color and cf(y, x + 1) == " ":
                score += 50
            if cf(y, x + 1) == my_color and cf(y, x + 2) == my_color and cf(y, x - 1) == " ":
                score += 30

        place_piece(x, my_color)
        if check_for_win(my_color):
            score -= 200
            gb1 = copy.deepcopy(reset_gb)
            place_piece(x, my_color)
            place_piece(x, opponent_col)
            place_piece(x, my_color)
            if check_for_win(my_color):
                score += 120
        gb1 = copy.deepcopy(reset_gb)
        place_piece(x, my_color)
        place_piece(x, opponent_col)
        if check_for_win(opponent_col):
            score -= 200

        # check for opponent piece
        gb1 = copy.deepcopy(reset_gb)
        y = place_piece(x, opponent_col)
        if check_for_win(opponent_col):
            score += 490
        if x in [1, 2, 3, 4]:
            if cf(y, x - 1) == opponent_col or cf(y, x + 1) == opponent_col:
                score += 30

        gb1 = copy.deepcopy(reset_gb)

        move_options.append([score, x + 1])
    # print(move_options)
    return sort_choices(move_options)
