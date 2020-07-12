import random
import time
from graphics import ship_missed
from graphics import ship_hit
from graphics import game_title


def get_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('0')
    return board


def blank_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('0')
    return board


def get_move(user_move, board):
    typed_move = (0, 0)

    dict = {}
    limit = len(board[0])

    for i in range(limit):
        dict[chr(65+i)] = i
    # print(dict)

    while True:
        if user_move == 'quit':
            quit()

        user_move_list = list(user_move)
        if user_move_list[0] in dict and user_move_list[1].isnumeric() and int(user_move_list[1]) <= 5:
            typed_move = (dict[user_move_list[0]], int(user_move_list[1])-1)

            if board[typed_move[0]][typed_move[1]] == '0':
                return typed_move
            else:
                return typed_move

        else:
            user_move = input('Type a valid move: ').upper()


def mark(board, row, col):

    try:
        board[row][col] = 'X'
        return board
    except:
        print('error')


def display_board(board):

    row_count = len(board)
    col_count = len(board[0])
    for i in range(row_count):
        print(f'  {i+1}  ', end='')
    print()
    print()
    for i in range(row_count):
        row_to_print = chr(65 + i)
        for j in range(col_count):
            row_to_print += ' ' + board[i][j] + " | "
        print(f'{row_to_print}')
        print('----+' * row_count)


def player1_placing_ship(size, ship_size):
    print('        PLAYER 1' + '\n')
    board = get_board(size)
    print('Player 1 place your ship! \n')
    display_board(board)
    turn = True
    while turn:
        for i in range(ship_size):
            position = input('Enter ship placement: ').upper()
            move = get_move(position, board)
            game_board = mark(board, move[0], move[1])
            display_board(game_board)
        turn = False
    display_board(game_board)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    return game_board


def player2_placing_ship(size, ship_size):
    print('        PLAYER 2' + '\n')
    board = get_board(size)
    print('Player 2 place your ship! \n')
    display_board(board)
    turn = True
    while turn:
        for i in range(ship_size):
            position = input('Enter ship placement: ').upper()
            move = get_move(position, board)
            game_board = mark(board, move[0], move[1])
            display_board(game_board)
        turn = False
    display_board(game_board)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    return game_board


def ai_placing_ship(size, ship_size):
    print('         PLAYER 3')
    board = get_board(size)
    for i in range(ship_size):
        x = random.randint(0, len(board))
        y = random.randint(0, len(board))
        poz = (x, y)
        poz2 = tuple(poz)
        board[poz2[0] - 1][poz2[1] - 1] = 'X'

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    # print(board)
    return board


def random_row(board):
    return random.randint(0, len(board)-1)


def random_col(board):
    return random.randint(0, len(board[0])-1)


def player_vs_player():
    turns_between_5_and_50 = True
    size_of_grid_between_5_and_10 = True
    ship_size_between_2_and_4 = True
    while turns_between_5_and_50:
        try:
            turns = int(input('How many chances would you like to have?: '))
            if turns >= 5 and turns <= 50:
                break
            else:
                print('You must choose between 5 and 50')
                turns = int(
                    input('How many chances would you like to have?: '))
        except ValueError:
            print('Please enter a number')

    while size_of_grid_between_5_and_10:
        try:
            size = int(input('Enter size of grid: '))
            if size >= 5 and size <= 10:
                break
            else:
                print('Grid size must be between 5 and 10')
                size = int(input('Enter size of grid: '))
        except ValueError:
            print('Please enter a number')

    while ship_size_between_2_and_4:
        try:
            ship_size = int(input('Enter size of ships: '))
            if ship_size >= 2 and ship_size <= 4:
                break
            else:
                print('Ship size must be between 2 and 4')
                ship_size = int(input('Enter size of ships: '))
        except ValueError:
            print('Please enter a number')

# -----------------------------------------------------

    print('\n\n')
    player1_ship_board = player1_placing_ship(size, ship_size)
    player2_ship_board = player2_placing_ship(size, ship_size)
    player1_blank_grid = blank_board(size)
    player2_blank_grid = blank_board(size)
    print('\n\n')
    player1_turn = True
    game_on = True
    player1_has_won_count = 0
    player2_has_won_count = 0
    player1_turn_count = turns
    player2_turn_count = turns
    while game_on:
        while player1_turn:
            time.sleep(1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('      PLAYER 1 TURN' + '\n')
            print(f'You have {player1_turn_count} more turns!')
            print()
            display_board(player1_blank_grid)
            # side_by_side_grid(z1, z2)
            position = input('Enter position: ').upper()
            move = get_move(position, player2_ship_board)
            if player2_ship_board[move[0]][move[1]] == 'X':
                player1_blank_grid[move[0]][move[1]] = 'H'
                display_board(player1_blank_grid)
                ship_hit()
                player1_has_won_count += 1
                player1_turn_count -= 1
                if player1_has_won_count == ship_size:
                    print('PLAYER 1 WON THE GAME!')
                    quit()
                if player1_turn_count == 1:
                    print('You have 1 more chance !')
                if player1_turn_count == 0:
                    print(
                        f"It'\s a draw !You had {turns} chances !")
                    quit()
                    game_on = False
                player1_turn = False
            else:
                player1_blank_grid[move[0]][move[1]] = 'M'
                display_board(player1_blank_grid)
                ship_missed()
                player1_turn_count -= 1
                if player1_turn_count == 1:
                    print('You have 1 more chance !')
                if player1_turn_count == 0:
                    print(
                        f"It'\s a draw !You had {turns} chances !")
                    quit()
                player1_turn = False
        while not player1_turn:
            time.sleep(1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('      PLAYER 2 TURN' + '\n')
            print(f'You have {player2_turn_count} more turns!')
            print()
            display_board(player2_blank_grid)
            # side_by_side_grid(z1, z2)
            position = input('Enter position: ').upper()
            move = get_move(position, player1_ship_board)
            if player1_ship_board[move[0]][move[1]] == 'X':
                player2_blank_grid[move[0]][move[1]] = 'H'
                display_board(player2_blank_grid)
                # side_by_side_grid(z1, z2)
                print('HIT!')
                player2_has_won_count += 1
                player2_turn_count -= 1
                if player2_has_won_count == ship_size:
                    print('PLAYER 2 WON THE GAME! ')
                    quit()
                if player2_turn_count == 1:
                    print('You have 1 more chance !')
                if player2_turn_count == 0:
                    print(
                        f"It'\s a draw !You had {turns} chances !")
                    quit()
                    game_on = False
                player1_turn = True
            else:
                player2_blank_grid[move[0]][move[1]] = 'M'
                display_board(player2_blank_grid)
                ship_missed()
                player2_turn_count -= 1
                if player2_turn_count == 1:
                    print('You have 1 more chance !')
                if player2_turn_count == 0:
                    print(
                        f"It'\s a draw !You had {turns} chances !")
                    quit()
                player1_turn = True


def player_vs_ai():
    turns_between_5_and_50 = True
    size_of_grid_between_5_and_10 = True
    ship_size_between_2_and_4 = True
    while turns_between_5_and_50:
        try:
            turns = int(
                input('How many chances would you like to have?: '))
            if turns >= 5 and turns <= 50:
                break
            else:
                print('You must choose between 5 and 50')
                turns = int(
                    input('How many chances would you like to have?: '))
        except ValueError:
            print('Please enter a number')

    while size_of_grid_between_5_and_10:
        try:
            size = int(input('Enter size of grid: '))
            if size >= 5 and size <= 10:
                break
            else:
                print('Grid size must be between 5 and 10')
                size = int(input('Enter size of grid: '))
        except ValueError:
            print('Please enter a number')

    while ship_size_between_2_and_4:
        try:
            ship_size = int(input('Enter size of ships: '))
            if ship_size >= 2 and ship_size <= 4:
                break
            else:
                print('Ship size must be between 2 and 4')
                ship_size = int(input('Enter size of ships: '))
        except ValueError:
            print('Please enter a number')

    player1_blank_grid = blank_board(size)
    ai_ship_board = ai_placing_ship(size, ship_size)
    print('\n\n')
    player1_turn = True
    game_on = True
    player1_turn_count = turns
    has_won_count = 0
    while game_on:
        while player1_turn:
            time.sleep(1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('      PLAYER 1 TURN' + '\n')
            print(f'You have {player1_turn_count} more turns!')
            display_board(player1_blank_grid)
            position = input('Enter position: ').upper()
            move = get_move(position, ai_ship_board)
            if ai_ship_board[move[0]][move[1]] == 'X':
                player1_blank_grid[move[0]][move[1]] = 'H'
                display_board(player1_blank_grid)
                print('HIT!')
                has_won_count += 1
                player1_turn_count -= 1
                if has_won_count == ship_size:
                    print('PLAYER 1 WON THE GAME!')
                    quit()
                if player1_turn_count == 1:
                    print('You have 1 more chance !')
                if player1_turn_count == 0:
                    print(f'Game Over ! You had {turns} chances !')
                    print('AI WON!')
                    quit()
                    game_on = False
            else:
                player1_blank_grid[move[0]][move[1]] = 'M'
                print('\n\n\n\n')
                display_board(player1_blank_grid)
                print()
                ship_missed()
                player1_turn_count -= 1
                if player1_turn_count == 1:
                    print('You have 1 more chance !')
                if player1_turn_count == 0:
                    print(f'Game Over ! You had {turns} chances !')
                    print('AI WON!')
                    quit()


def ai_vs_ai():
    turns_between_5_and_50 = True
    size_of_grid_between_5_and_10 = True
    ship_size_between_2_and_4 = True
    while turns_between_5_and_50:
        try:
            turns = int(
                input('How many chances would you like to have?: '))
            if turns >= 5 and turns <= 50:
                break
            else:
                print('You must choose between 5 and 50')
                turns = int(
                    input('How many chances would you like to have?: '))
        except ValueError:
            print('Please enter a number')

    while size_of_grid_between_5_and_10:
        try:
            size = int(input('Enter size of grid: '))
            if size >= 5 and size <= 10:
                break
            else:
                print('Grid size must be between 5 and 10')
                size = int(input('Enter size of grid: '))
        except ValueError:
            print('Please enter a number')

    while ship_size_between_2_and_4:
        try:
            ship_size = int(input('Enter size of ships: '))
            if ship_size >= 2 and ship_size <= 4:
                break
            else:
                print('Ship size must be between 2 and 4')
                ship_size = int(input('Enter size of ships: '))
        except ValueError:
            print('Please enter a number')

    player1_blank_grid = blank_board(size)
    ai_ship_board = ai_placing_ship(size, ship_size)
    print('\n\n')
    player1_turn = True
    game_on = True
    has_won_count = 0
    ai_turn_count = turns
    while game_on:
        while player1_turn:
            time.sleep(1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('AI TURN!')
            print(f'You have {ai_turn_count} more turns!')
            print()
            display_board(player1_blank_grid)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            x = (random_row(ai_ship_board),
                 random_col(ai_ship_board))
            position = tuple(x)
            if ai_ship_board[position[0]][position[1]] == 'X':
                if player1_blank_grid[position[0]][position[1]] == 'H':
                    player1_blank_grid[position[0 + 1]][position[1]] = 'H'
                else:
                    player1_blank_grid[position[0]][position[1]] = 'H'
                display_board(player1_blank_grid)
                ship_hit()
                has_won_count += 1
                ai_turn_count -= 1
                if has_won_count == ship_size:
                    display_board(player1_blank_grid)
                    print('WE HAVE A WINNER! ')
                    quit()
                if ai_turn_count == 1:
                    print('You have 1 more chance !')
                if ai_turn_count == 0:
                    print(f'Game Over ! You had {turns} chances !')
                    quit()
                    game_on = False
            else:
                if player1_blank_grid[position[0]][position[1]] != 'M' and player1_blank_grid[position[0]][position[1]] != 'H':
                    player1_blank_grid[position[0]][position[1]] = 'M'
                print(f'You have {ai_turn_count} more turns!')
                display_board(player1_blank_grid)
                # print('MISSED')
                ship_missed()
                print()
                ai_turn_count -= 1
                if ai_turn_count == 1:
                    print('You have 1 more chance !')
                if ai_turn_count == 0:
                    print(f'Game Over ! Out of turns !')
                    quit()


def main():
    print('\n\n\n\n\n\n\n\n')
    game_title()
    print()
    print('1.Multiplayer' + '\n\n' + '2.Single player' +
          '\n\n' + '3.Watch a game' + '\n\n')
    while True:
        choice = input('Choose game mode: ')
        if choice == '1':
            player_vs_player()
        if choice == '2':
            player_vs_ai()
        if choice == '3':
            ai_vs_ai()
        else:
            print('This game mode does not exist')


if __name__ == "__main__":
    main()
