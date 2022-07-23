import random
import copy


def bot_move(gb, bot_marker, user_marker, blank_spots):
    def check_open_columns():
        global safe_spots
        global bot_marker
        for y in range(7):
            if gb[0][y] != ' ':
                safe_spots.remove(y + 1)

    def check_almost_win(marker):
        global safe_spots
        # Vertical Three in a Row:
        global bot_already_played
        global bot_marker
        global bot_choice

        for x in range(0, 3):
            for y in range(7):
                if gb[x + 3][y] == gb[x + 2][y] == gb[x + 1][y] == marker and gb[x][y] == ' ':
                    bot_choice = y + 1
                    bot_already_played = True

        if bot_already_played == False:
            # Horizontal Three in a Row Check (Left to Right):
            for x in range(6):
                for y in range(4):
                    if gb[x][y] == gb[x][y + 1] == gb[x][y + 2] == marker and gb[x][y + 3] == ' ':
                        if x == 5:
                            bot_choice = y + 4
                            bot_already_played = True

                        if x == 4:
                            if gb[x + 1][y + 3] != ' ':
                                bot_choice = y + 4
                                bot_already_played = True
                            else:
                                if (y + 4) in safe_spots:
                                    safe_spots.remove(y + 4)

                        if x in [0, 1, 2, 3]:
                            if gb[x + 1][y + 3] != ' ':
                                bot_choice = y + 4
                                bot_already_played = True
                            if gb[x + 2][y + 3] != ' ':
                                if (y + 4) in safe_spots:
                                    safe_spots.remove(y + 4)

        if bot_already_played == False:
            # Horizontal Three in a Row Check (Right to Left):
            for x in range(6):
                for y in range(3, 7):
                    if gb[x][y] == gb[x][y - 1] == gb[x][y - 2] == marker and gb[x][y - 3] == ' ':
                        if x == 5:
                            bot_choice = y - 2
                            bot_already_played = True

                        if x == 4:
                            if gb[x + 1][y - 3] != ' ':
                                bot_choice = y - 2
                                bot_already_played = True

                            else:
                                if (y - 2) in safe_spots:
                                    safe_spots.remove(y - 2)

                        if x in [0, 1, 2, 3]:
                            if gb[x + 1][y - 3] != ' ':
                                bot_choice = y - 2
                                bot_already_played = True
                            if gb[x + 2][y - 3] != ' ':
                                if (y - 2) in safe_spots:
                                    safe_spots.remove(y - 2)

        if bot_already_played == False:
            # Two in a Row, Blank, One check:
            for x in range(6):
                for y in range(4):
                    if gb[x][y] == gb[x][y + 1] == gb[x][y + 3] == marker and gb[x][y + 2] == ' ':
                        if x == 5:
                            bot_choice = y + 3
                            bot_already_played = True
                        if x == 4:
                            if gb[x + 1][y + 2] != ' ':
                                bot_choice = y + 3
                                bot_already_played = True
                            else:
                                if (y + 3) in safe_spots:
                                    safe_spots.remove(y + 3)
                        if x in range(0, 4):
                            if gb[x + 1][y + 2] != ' ':
                                bot_choice = y + 3
                                bot_already_played = True
                            if gb[x + 2][y + 2] != ' ':
                                if (y + 3) in safe_spots:
                                    safe_spots.remove(y + 3)

        if bot_already_played == False:
            # One, Blank, Two in a Row check:
            for x in range(6):
                for y in range(4):
                    if gb[x][y] == gb[x][y + 2] == gb[x][y + 3] == marker and gb[x][y + 1] == ' ':
                        if x == 5:
                            bot_choice = y + 2
                            bot_already_played = True
                        if x == 4:
                            if gb[x + 1][y + 1] != ' ':
                                bot_choice = y + 2
                                bot_already_played = True
                            else:
                                if (y + 2) in safe_spots:
                                    safe_spots.remove(y + 2)
                        if x in range(0, 4):
                            if gb[x + 1][y + 1] != ' ':
                                bot_choice = y + 2
                                bot_already_played = True
                            if gb[x + 2][y + 1] != ' ':
                                if (y + 2) in safe_spots:
                                    safe_spots.remove(y + 2)

        if bot_already_played == False:
            # Three in a Row Diagonal (Left to Right going up):
            for x in range(3, 6):
                for y in range(4):
                    if gb[x][y] == gb[x - 1][y + 1] == gb[x - 2][y + 2] == marker and gb[x - 3][y + 3] == ' ':
                        if gb[x - 2][y + 3] != ' ':
                            bot_choice = y + 4
                            bot_already_played = True
                        if gb[x - 1][y + 3] != ' ':
                            if (y + 4) in safe_spots:
                                safe_spots.remove(y + 4)

        if bot_already_played == False:
            # Three in a Row Diagonal (Right to Left going up):
            for x in range(3, 6):
                for y in range(3, 7):
                    if gb[x][y] == gb[x - 1][y - 1] == gb[x - 2][y - 2] == marker and gb[x - 3][y - 3] == ' ':
                        if gb[x - 2][y - 3] != ' ':
                            bot_choice = y - 2
                            bot_already_played = True
                        if gb[x - 1][y - 3] != ' ':
                            if (y - 2) in safe_spots:
                                safe_spots.remove(y - 2)

        if bot_already_played == False:
            # Two in a Row, Blank, One Diagonal (Left to Right going up):
            for x in range(3, 6):
                for y in range(4):
                    if gb[x][y] == gb[x - 1][y + 1] == gb[x - 3][y + 3] == marker and gb[x - 2][y + 2] == ' ':
                        if gb[x - 1][y + 2] != ' ':
                            bot_choice = y + 3
                            bot_already_played = True
                        if gb[x][y + 2] != ' ':
                            if (y + 3) in safe_spots:
                                safe_spots.remove(y + 3)

        if bot_already_played == False:
            # Two in a Row, Blank, One Diagonal (Right to Left going up):
            for x in range(3, 6):
                for y in range(3, 7):
                    if gb[x][y] == gb[x - 1][y - 1] == gb[x - 3][y - 3] == marker and gb[x - 2][y - 2] == ' ':
                        if gb[x - 1][y - 2] != ' ':
                            bot_choice = y - 1
                            bot_already_played = True
                        if gb[x][y - 2] != ' ':
                            if (y - 1) in safe_spots:
                                safe_spots.remove(y - 1)

        if bot_already_played == False:
            # One, Blank, Two in a Row (Left to Right going up):
            for x in range(3, 6):
                for y in range(4):
                    if gb[x][y] == gb[x - 2][y + 2] == gb[x - 3][y + 3] == marker and gb[x - 1][y + 1] == ' ':
                        if x == 5:
                            if gb[x][y + 1] != ' ':
                                bot_choice = y + 2
                                bot_already_played = True
                            else:
                                if (y + 2) in safe_spots:
                                    safe_spots.remove(y + 2)
                        if x in range(0, 5):
                            if gb[x][y + 1] != ' ':
                                bot_choice = y + 2
                                bot_already_played = True
                            if gb[x + 1][y + 1] != ' ':
                                if (y + 2) in safe_spots:
                                    safe_spots.remove(y + 2)

        if bot_already_played == False:
            # One, Blank, Two in a Row (Right to Left going up):
            for x in range(3, 6):
                for y in range(3, 7):
                    if gb[x][y] == gb[x - 2][y - 2] == gb[x - 3][y - 3] == marker and gb[x - 1][y - 1] == ' ':
                        if x == 5:
                            if gb[x][y - 1] != ' ':
                                bot_choice = y
                                bot_already_played = True
                            else:
                                if y in safe_spots:
                                    safe_spots.remove(y)
                        if x in range(0, 5):
                            if gb[x][y - 1] != ' ':
                                bot_choice = y
                                bot_already_played = True
                            else:
                                if gb[x + 1][y - 1] != ' ':
                                    if y in safe_spots:
                                        safe_spots.remove(y)

    def check_super_trap(marker):
        global bot_already_played
        global bot_marker
        global bot_choice

        for y in range(1, 4):
            if gb[5][y] == gb[5][y + 1] == marker:
                if gb[5][y - 1] == gb[5][y + 2] == gb[0][y + 3] == ' ':
                    bot_choice = y + 3
                    bot_already_played = True
        if bot_already_played == False:
            for y in range(2, 5):
                if gb[5][y] == gb[5][y + 1] == marker:
                    if gb[5][y - 1] == gb[5][y - 2] == ' ':
                        if gb[5][y + 2] == ' ':
                            bot_choice = y
                            bot_already_played = True

    def explore_hypothetical_moves(marker):
        global safe_spots
        for y in safe_spots:
            place_hypothetical_piece(y, marker)

    def place_hypothetical_piece(y, marker):
        global hgb
        array_column = y - 1
        already_played = False
        grabbed_x = 0

        for x in range(1, 6):
            if hgb[x][array_column] != ' ' and already_played == False:
                hgb[x - 1][array_column] = marker
                grabbed_x = x - 1
                already_played = True

        if already_played == False:
            hgb[5][array_column] = marker
            grabbed_x = 5
            already_played = True

        check_for_three(grabbed_x, array_column, marker)
        hgb = copy.deepcopy(gb)

    def check_for_three(x, y, marker):
        global good_plays
        # Vertical three in a row:
        if x in range(1, 4):
            if hgb[x][y] == hgb[x + 1][y] == hgb[x + 2][y] == marker and hgb[x - 1][y] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Horizontal Combos:
        # Y, A, A, Blank:
        if y in range(0, 4):
            if hgb[x][y] == hgb[x][y + 1] == hgb[x][y + 2] == marker and hgb[x][y + 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Y, A, Blank A:
        if y in range(0, 4):
            if hgb[x][y] == hgb[x][y + 1] == hgb[x][y + 3] == marker and hgb[x][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

            # Y, Blank, A, A:
            if y in range(0, 4):
                if hgb[x][y] == hgb[x][y + 2] == hgb[x][y + 3] == marker and hgb[x][y + 1] == ' ':
                    if (y + 1) not in good_plays:
                        good_plays.append(y + 1)

        # A, Y, A, Blank:
        if y in range(1, 5):
            if hgb[x][y - 1] == hgb[x][y] == hgb[x][y + 1] == marker and hgb[x][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Y, Blank, A:
        if y in range(1, 5):
            if hgb[x][y - 1] == hgb[x][y] == hgb[x][y + 2] == marker and hgb[x][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Y, Blank:
        if y in range(2, 6):
            if hgb[x][y - 2] == hgb[x][y - 1] == hgb[x][y] == marker and hgb[x][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Blank, Y:
        if y in range(3, 7):
            if hgb[x][y - 3] == hgb[x][y - 2] == hgb[x][y] == marker and hgb[x][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, A, Y:
        if y in range(3, 7):
            if hgb[x][y - 3] == hgb[x][y - 1] == hgb[x][y] == marker and hgb[x][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, Y, A:
        if y in range(2, 6):
            if hgb[x][y - 2] == hgb[x][y] == hgb[x][y + 1] == marker and hgb[x][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, Y, A, A:
        if y in range(1, 5):
            if hgb[x][y] == hgb[x][y + 1] == hgb[x][y + 2] == marker and hgb[x][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, Y, A:
        if y in range(2, 6):
            if hgb[x][y - 1] == hgb[x][y] == hgb[x][y + 1] == marker and hgb[x][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, A, Y:
        if y in range(3, 7):
            if hgb[x][y - 2] == hgb[x][y - 1] == hgb[x][y] == marker and hgb[x][y - 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Diagonals (Left to Right going up):
        # Y, A, A, Blank:
        if y in range(0, 4) and x in range(3, 6):
            if hgb[x][y] == hgb[x - 1][y + 1] == hgb[x - 2][y + 2] == marker and hgb[x - 3][y + 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Y, A, Blank A:
        if y in range(0, 4) and x in range(3, 6):
            if hgb[x][y] == hgb[x - 1][y + 1] == hgb[x - 3][y + 3] == marker and hgb[x - 2][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

            # Y, Blank, A, A:
            if y in range(0, 4) and x in range(3, 6):
                if hgb[x][y] == hgb[x - 2][y + 2] == hgb[x - 3][y + 3] == marker and hgb[x - 1][y + 1] == ' ':
                    if (y + 1) not in good_plays:
                        good_plays.append(y + 1)

        # A, Y, A, Blank:
        if y in range(1, 5) and x in range(2, 5):
            if hgb[x + 1][y - 1] == hgb[x][y] == hgb[x - 1][y + 1] == marker and hgb[x - 2][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Y, Blank, A:
        if y in range(1, 5) and x in range(2, 5):
            if hgb[x + 1][y - 1] == hgb[x][y] == hgb[x - 2][y + 2] == marker and hgb[x - 1][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Y, Blank:
        if y in range(2, 6) and x in range(1, 4):
            if hgb[x + 2][y - 2] == hgb[x + 1][y - 1] == hgb[x][y] == marker and hgb[x - 1][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Blank, Y:
        if y in range(3, 7) and x in range(0, 3):
            if hgb[x + 3][y - 3] == hgb[x + 2][y - 2] == hgb[x][y] == marker and hgb[x + 1][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, A, Y:
        if y in range(3, 7) and x in range(0, 3):
            if hgb[x + 3][y - 3] == hgb[x + 1][y - 1] == hgb[x][y] == marker and hgb[x + 2][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, Y, A:
        if y in range(2, 6) and x in range(1, 4):
            if hgb[x + 2][y - 2] == hgb[x][y] == hgb[x - 1][y + 1] == marker and hgb[x + 1][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, Y, A, A:
        if y in range(1, 5) and x in range(2, 5):
            if hgb[x][y] == hgb[x - 1][y + 1] == hgb[x - 2][y + 2] == marker and hgb[x + 1][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, Y, A:
        if y in range(2, 6) and x in range(1, 4):
            if hgb[x + 1][y - 1] == hgb[x][y] == hgb[x - 1][y + 1] == marker and hgb[x + 2][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, A, Y:
        if y in range(3, 7) and x in range(0, 3):
            if hgb[x + 2][y - 2] == hgb[x + 1][y - 1] == hgb[x][y] == marker and hgb[x + 3][y - 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Diagonals (Right to Left going up):
        # Y, A, A, Blank:
        if y in range(3, 7) and x in range(3, 6):
            if hgb[x][y] == hgb[x - 1][y - 1] == hgb[x - 2][y - 2] == marker and hgb[x - 3][y - 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Y, A, Blank A:
        if y in range(3, 7) and x in range(3, 6):
            if hgb[x][y] == hgb[x - 1][y - 1] == hgb[x - 3][y - 3] == marker and hgb[x - 2][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

            # Y, Blank, A, A:
            if y in range(3, 7) and x in range(3, 6):
                if hgb[x][y] == hgb[x - 2][y - 2] == hgb[x - 3][y - 3] == marker and hgb[x - 1][y - 1] == ' ':
                    if (y + 1) not in good_plays:
                        good_plays.append(y + 1)

        # A, Y, A, Blank:
        if y in range(2, 6) and x in range(2, 5):
            if hgb[x + 1][y + 1] == hgb[x][y] == hgb[x - 1][y - 1] == marker and hgb[x - 2][y - 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Y, Blank, A:
        if y in range(2, 6) and x in range(2, 5):
            if hgb[x + 1][y + 1] == hgb[x][y] == hgb[x - 2][y - 2] == marker and hgb[x - 1][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Y, Blank:
        if y in range(1, 5) and x in range(1, 4):
            if hgb[x + 2][y + 2] == hgb[x + 1][y + 1] == hgb[x][y] == marker and hgb[x - 1][y - 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, A, Blank, Y:
        if y in range(0, 4) and x in range(0, 3):
            if hgb[x + 3][y + 3] == hgb[x + 2][y + 2] == hgb[x][y] == marker and hgb[x + 1][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, A, Y:
        if y in range(0, 4) and x in range(0, 3):
            if hgb[x + 3][y + 3] == hgb[x + 1][y + 1] == hgb[x][y] == marker and hgb[x + 2][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # A, Blank, Y, A:
        if y in range(1, 5) and x in range(1, 4):
            if hgb[x + 2][y + 2] == hgb[x][y] == hgb[x - 1][y - 1] == marker and hgb[x + 1][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, Y, A, A:
        if y in range(2, 6) and x in range(2, 5):
            if hgb[x][y] == hgb[x - 1][y - 1] == hgb[x - 2][y - 2] == marker and hgb[x + 1][y + 1] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, Y, A:
        if y in range(1, 5) and x in range(1, 4):
            if hgb[x + 1][y + 1] == hgb[x][y] == hgb[x - 1][y - 1] == marker and hgb[x + 2][y + 2] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

        # Blank, A, A, Y:
        if y in range(0, 4) and x in range(0, 3):
            if hgb[x + 2][y + 2] == hgb[x + 1][y + 1] == hgb[x][y] == marker and hgb[x + 3][y + 3] == ' ':
                if (y + 1) not in good_plays:
                    good_plays.append(y + 1)

    global safe_spots
    global bot_already_played
    global good_plays
    global bot_choice

    catch_phrase_choice = random.randint(1, 4)
    if catch_phrase_choice == 1:
        print('\nHmmmm, so many spaces to choose from \n')
    if catch_phrase_choice == 2:
        print('\nCalculating optimal strategy...\n')
    if catch_phrase_choice == 3:
        print('\nI am the Michael Jordan of Connect Four\n')
    if catch_phrase_choice == 4:
        print('\nI\'ll just roll a dice to choose where to play...\n')

    bot_already_played = False

    safe_spots = [1, 2, 3, 4, 5, 6, 7]
    good_plays = []
    check_open_columns()

    check_almost_win(bot_marker)

    if bot_already_played == False:
        check_almost_win(user_marker)

    if bot_already_played == False:
        check_super_trap(user_marker)
        check_super_trap(bot_marker)

    if bot_already_played == False:
        global hgb
        hgb = copy.deepcopy(gb)
        explore_hypothetical_moves(bot_marker)
        explore_hypothetical_moves(user_marker)

    if bot_already_played == False:
        if blank_spots in [40, 41, 42]:
            bot_choice = 4
        else:
            if len(good_plays) > 0:
                bot_choice = random.choice(good_plays)
            else:
                if len(safe_spots) > 0:
                    open_spot_check = False
                    while open_spot_check == False:
                        bot_choice = random.choice(safe_spots)
                        if gb[0][bot_choice - 1] == ' ':
                            open_spot_check = True
                if len(safe_spots) == 0:
                    open_spot_check = False
                    while open_spot_check == False:
                        bot_choice = random.randint(1, 7)
                        if gb[0][bot_choice - 1] == ' ':
                            open_spot_check = True

    return (bot_choice)
