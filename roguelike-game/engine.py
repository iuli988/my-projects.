import dictionaries as d
import util
import random
import time
inventory = {}
gate_1 = {
    'type': 'ingridient',
    'item_icon': '⛩️ ',
    'position_x': 9,
    'position_y': 8,
    'number': 1,
    'board': 1,
    'added_power': 0,
    'added_protection': 10
    }
gate_2 = {
    'type': 'ingridient',
    'item_icon': '🌁 ',
    'position_x': 9,
    'position_y': 8,
    'number': 1,
    'board': 2,
    'added_power': 0,
    'added_protection': 10
    }
gate_3 = {
    'type': 'ingridient',
    'item_icon': '🚪 ',
    'position_x': 9,
    'position_y': 8,
    'number': 1,
    'board': 3,
    'added_power': 0,
    'added_protection': 0
    }
player = {
    'player_icon': '😋',
    'position_x': 6,
    'position_y': 4,
    'player_life': 20,
    'player_power': 6,
    'used_code': False,
    'wins': 0,
    'loss': 0,
    'levels': 1
    }
boss = {
    'other_type': "enemy",
    'other_name': "Boss",
    'player_icon': "🤑",
    'position_x': 3,
    'position_y': 5,
    'step': 1,
    'health': 8,
    'goal_quiz': "winning",
    'questions': [],
    'width': 5,
    'power': 10,
    'board': 3
    }
little_boss_1 = {
    'other_type': "quiz",
    'other_name': "HATZ.UL SUPREM",
    'player_icon': "🐭",
    'position_x': 5,
    'position_y': 5,
    'step': 1,
    'health': 1,
    'goal_quiz': "Syringe",
    'questions':   [["What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n", "b", False],
                    ["Which river passes through Bucharest?\n(a) Tisa\n(b) Dâmbovița\n(c) Danube\n", "c", False],
                    ["What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n", "c", False],
                    ["What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n", "b", False],
                    ["Which European country shares a border with Brazil?\n(a) Germany\n(b) Belgium\n(c) France\n", "b", False]],
    'width': 1,
    'power': 4,
    'board': 1
}

little_boss_2 = {
    'other_type': "quiz",
    'other_name': "HATZ.UL SUPREM",
    'player_icon': "🐮",
    'position_x': 5,
    'position_y': 5,
    'step': 1,
    'health': 10,
    'goal_quiz': "Syringe",
    'questions':   [["What's the first name of 'Ooops I did it again' singer?\n(a) Christina\n(b) Britney\n(c) Jessica\n", "b", False],
                    ["Which river passes through Bucharest?\n(a) Tisa\n(b) Dâmbovița\n(c) Danube\n", "c", False],
                    ["What color are bananas?\n(a) Red\n(b) Orange\n(c) Yellow\n", "c", False],
                    ["What is the capital of Australia?\n(a) Sydney\n(b) Canberra\n(c) Melbourne\n", "b", False],
                    ["Which European country shares a border with Brazil?\n(a) Germany\n(b) Belgium\n(c) France\n", "b", False]],
    'width': 1,
    'power': 4,
    'board': 1
}


def print_board(board):
    for row in board:
        print(' '.join(row))


def create_board(width=10, height=10, border_color='🧱', fill_color='  '):
    board = []
    list_range_of_border_widith = []

    for x in range(width):
        board.append(["1"]*height)

    if border_color != 1:

        for i in range(width):
            board[i][height - 1] = str(border_color)
            board[i][0] = str(border_color)

        for j in range(height):
            board[0][j] = str(border_color)
            board[width - 1][j] = str(border_color)

    if fill_color != 1:

        for i in range(1, width - 1):

            for j in range(1, height - 1):
                board[i][j] = str(fill_color)

    for i in range(min(int(width / 2), int(height / 2))):
        list_range_of_border_widith.append(i)
    list_range_of_border_widith.remove(0)

    return board





def put_player_on_board(board, player, items=d.items):
    board[player['position_x']][player['position_y']] = player['player_icon']
    return board, player['position_x'], player['position_y']


BOARD_1 = create_board()
BOARD_1, x, y = put_player_on_board(BOARD_1, little_boss_1)
BOARD_2 = create_board()
BOARD_2,x ,y = put_player_on_board(BOARD_2, little_boss_2)
BOARD_3 = create_board()
BOARD_3, x, y = put_player_on_board(BOARD_3, boss)


def items_and_coordonates_that_u_can_use(board, items=d.items):
    items_that_u_can_use = {}
    coordonate_of_items_that_u_can_use = []
    # nr_board = nr_of_the_board(board)
    if board == BOARD_1:
        for element in d.items:
            if 1 == items[element]['board']:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                if element in items_that_u_can_use:
                    items_that_u_can_use[element] += 1
                else:
                    items_that_u_can_use[element] = 1
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)
    if board == BOARD_2:
        for element in d.items:
            if 2 == items[element]['board']:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                if element in items_that_u_can_use:
                    items_that_u_can_use[element] += 1
                else:
                    items_that_u_can_use[element] = 1
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)
    if board == BOARD_3:
        for element in d.items:
            if 3 == items[element]['board']:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                if element in items_that_u_can_use:
                    items_that_u_can_use[element] += 1
                else:
                    items_that_u_can_use[element] = 1
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)
    return items_that_u_can_use, coordonate_of_items_that_u_can_use


def put_items_on_every_type_of_board(board, items=d.items):
    items_that_u_can_use = []
    coordonate_of_items_that_u_can_use = []
    if board == BOARD_1:
        for element in d.items:
            if items[element]['board'] == 1:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                items_that_u_can_use.append(element)
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)

        for element in items_that_u_can_use:

            x = items[element]['position_x']
            y = items[element]['position_y']
            icon = items[element]['item_icon']

            board[x][y] = icon
    if board == BOARD_2:
        for element in d.items:
            if items[element]['board'] == 2:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                items_that_u_can_use.append(element)
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)

        for element in items_that_u_can_use:

            x = items[element]['position_x']
            y = items[element]['position_y']
            icon = items[element]['item_icon']

            board[x][y] = icon
    if board == BOARD_3:
        for element in d.items:
            if items[element]['board'] == 3:
                list_of_coordonates = ([items[element]['position_x'],
                                    items[element]['position_y']])

                items_that_u_can_use.append(element)
                coordonate_of_items_that_u_can_use.append(list_of_coordonates)

        for element in items_that_u_can_use:

            x = items[element]['position_x']
            y = items[element]['position_y']
            icon = items[element]['item_icon']

            board[x][y] = icon
    for row in board:
        print(" ".join(row))

    return board


def if_player_on_item(board, position_x_player, position_y_player, player,
                      items=d.items):
    global inventory
    items_u_will_use,coordonate_of_items_that_u_will_use = items_and_coordonates_that_u_can_use(board)

    for key in items_u_will_use:

        if items[key]['position_x'] == position_x_player and items[key]['position_y'] == position_y_player and ([items[key]['position_x'], items[key]['position_y']]) in coordonate_of_items_that_u_will_use:
            board[items[key]['position_x']][items[key]['position_y']] = player['player_icon']
            coordonate_of_items_that_u_will_use.remove([items[key]['position_x'], items[key]['position_y']])
            player['player_life'] += items[key]['added_protection']
            player['player_power'] += items[key]['added_power']

            if key in inventory:
                inventory[key] += 1
            else:
                inventory[key] = 1
    return inventory


def verify_if_it_is_on_border(board, player, width=10, height=10):

    for i in range(width):

        if (i == player['position_x']
            and height - 1 == player['position_y'])\
             or (i == player['position_x'] and 0 == player['position_y']):
            return True

    for j in range(height):

        if (0 == player['position_x']
            and j == player['position_y'])\
             or (width - 1 == player['position_x']
                 and j == player['position_y']):
            return True
    return False


def random_W_A_S_D(board, player):
    random_list = ["w", "a", "s", "d"]

    if board[player['position_x'] + 1][player['position_y']] != '  ':
        random_list.remove("s")
    if board[player['position_x'] - 1][player['position_y']] != '  ':
        random_list.remove("w")
    if board[player['position_x']][player['position_y'] + 1] != '  ':
        random_list.remove("d")
    if board[player['position_x']][player['position_y'] - 1] != '  ':
        random_list.remove("a")
    key = random.choice(random_list)
    if key == "w":
        player['position_x'] -= 1

        if verify_if_it_is_on_border(board, player) is False :
            board[player['position_x'] + 1][player['position_y']] = '  '
            put_player_on_board(board, player)

        else:
            player['position_x'] += 1
            key = random.choice(["w", "a", "s", "d"])

    elif key == "s":
        player['position_x'] += 1

        if verify_if_it_is_on_border(board, player) is False :
            board[player['position_x'] - 1][player['position_y']] = '  '
            put_player_on_board(board, player)

        else:
            player['position_x'] -= 1
            key = random.choice(["w", "a", "s", "d"])

    elif key == "a":
        player['position_y'] -= 1

        if verify_if_it_is_on_border(board, player) is False :
            board[player['position_x']][player['position_y'] + 1] = '  '
            put_player_on_board(board, player)

        else:
            player['position_y'] += 1
            key = random.choice(["w", "a", "s", "d"])

    elif key == "d":
        player['position_y'] += 1
        if verify_if_it_is_on_border(board, player) is False :
            board[player['position_x']][player['position_y'] - 1] = '  '
            put_player_on_board(board, player)

        else:
            player['position_y'] -= 1
            key = random.choice(["w", "a", "s", "d"])
    return board


def W_A_S_D(board, player):
    key = util.key_pressed()

    if key == "w" and board[player['position_x'] - 1][player['position_y']] != '🤑':
        player['position_x'] -= 1
        if verify_if_it_is_on_border(board, player) is False:
            board[player['position_x'] + 1][player['position_y']] = '  '
            put_player_on_board(board, player)
            util.clear_screen()
            print_board(board)
        elif verify_if_it_is_on_border(board, player) is True:
            player['position_x'] += 1
            key = util.key_pressed()

    elif key == "s" and board[player['position_x'] + 1][player['position_y']] != '🤑':
        player['position_x'] += 1

        if verify_if_it_is_on_border(board, player) is False:
            board[player['position_x'] - 1][player['position_y']] = '  '
            put_player_on_board(board, player)
            util.clear_screen()
            print_board(board)
        elif verify_if_it_is_on_border(board, player) is True:
            player['position_x'] -= 1
            key = util.key_pressed()

    elif key == "a" and board[player['position_x']][player['position_y'] - 1] != '🤑':
        player['position_y'] -= 1

        if verify_if_it_is_on_border(board, player) is False:
            board[player['position_x']][player['position_y'] + 1] = '  '
            put_player_on_board(board, player)
            util.clear_screen()
            print_board(board)
        elif verify_if_it_is_on_border(board, player) is True:
            player['position_y'] += 1
            key = util.key_pressed()

    elif key == "d" and board[player['position_x']][player['position_y'] + 1] != '🤑':
        player['position_y'] += 1

        if verify_if_it_is_on_border(board, player) is False:
            board[player['position_x']][player['position_y'] - 1] = '  '
            put_player_on_board(board, player)
            util.clear_screen()
            print_board(board)
        elif verify_if_it_is_on_border(board, player) is True:
            player['position_y'] -= 1
            key = util.key_pressed()
    # key = util.key_pressed()
    return board


def movement_and_damage(board, player, boss):
    # if board == BOARD_1:
    while player['player_life'] > 0:
        inventory = if_player_on_item(board, player['position_x'], player['position_y'], player)
        board = W_A_S_D(board, player)
        if (board[player['position_x'] + 1][player['position_y']] == '🤑' or
            board[player['position_x'] - 1][player['position_y']] == '🤑' or
            board[player['position_x']][player['position_y'] + 1] == '🤑' or
            board[player['position_x']][player['position_y'] - 1] == '🤑' or
            board[player['position_x'] + 1][player['position_y']] == '🐭' or
            board[player['position_x'] - 1][player['position_y']] == '🐭' or
            board[player['position_x']][player['position_y'] + 1] == '🐭' or
            board[player['position_x']][player['position_y'] - 1] == '🐭' or
            board[player['position_x'] + 1][player['position_y']] == '🐮' or
            board[player['position_x'] - 1][player['position_y']] == '🐮' or
            board[player['position_x']][player['position_y'] + 1] == '🐮' or
                board[player['position_x']][player['position_y'] - 1] == '🐮'):
            boss['health'] -= player['player_power']
            print(boss['health'])
            print(player['player_life'])
            if boss['health'] < 1:
                player['wins'] += 1
                if player['wins'] == 3:
                    print("YOU WIN!!!!")
                else:
                    print("You win this round")
            else:
                player['player_life'] -= boss['power']
                if player['player_life'] < 1:
                    print("You lost!!")
                    player['loss'] += 1
                    return False

            print("You have left with:")
            print(max(player['player_life'], 0))
        if boss['health'] > 0:
            board = random_W_A_S_D(board, boss)
        else:
            break
    return True


def create_final_board(board, boss):
    (board, x, y) = put_player_on_board(board, boss)
    board = put_items_on_every_type_of_board(board)
    (items_u_will_use,coordonate_of_items_that_u_will_use) = items_and_coordonates_that_u_can_use(board)
    return board, items_u_will_use, coordonate_of_items_that_u_will_use


def move_something_and_gate(board, player, boss, gate):
    while movement_and_damage(board, player, boss) == True:
        while player['position_x'] != gate['position_x'] - 1 or player['position_y'] != gate['position_y']:
            board = W_A_S_D(board, player)
            if boss['health'] < 1:
                (board, position_x_boss, position_y_boss) = put_player_on_board(board, boss)
                board[position_x_boss][position_y_boss] = '  '

        break


# BOARD_1, x, y = create_final_board(BOARD_1, little_boss_1)
# BOARD_2, x, y = create_final_board(BOARD_2, little_boss_2)
# BOARD_3, x, y = create_final_board(BOARD_2, boss)

# def main():
#     global BOARD_1
#     global BOARD_2
#     global BOARD_3
#     global items_u_will_use
#     print()
#     print("U entered first level")
#     print()

#     (BOARD_1, items_u_will_use, coordonate_of_items_that_u_will_use) = create_final_board(BOARD_1, little_boss_1)
#     (BOARD_1, x, y) = put_player_on_board(BOARD_1, little_boss_1)
#     move_something_and_gate(BOARD_1, player, little_boss_1, gate_1)

#     if player['player_life'] > 0:
#         print()
#         print("U entered second level")
#         print()

#     (BOARD_2,items_u_will_use, coordonate_of_items_that_u_will_use) = create_final_board(BOARD_2, little_boss_2)
#     move_something_and_gate(BOARD_2, player, little_boss_2, gate_2)

#     if player['player_life'] > 0:
#         print()
#         print("U entered the third level")
#         print()

#     (BOARD_3, items_u_will_use, coordonate_of_items_that_u_will_use) = create_final_board(BOARD_3, boss)
#     move_something_and_gate(BOARD_3, player, boss, gate_3)

# if __name__ == '__main__':
#     main()