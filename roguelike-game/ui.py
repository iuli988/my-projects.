def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()
    print()


def print_table(inventory):

    elements = sorted(inventory, key=inventory.get, reverse=True)
    print('-' * 17)
    print("{:>5} {:<2}".format('item name |', 'count'))
    print('-' * 17)

    for r in elements:
        results = (r, inventory[r])
        print("{:>12} {:>4}".format(r + ' | ', inventory[r]), end='\n')
    print('-' * 17)

    return ''


def print_player_essential_atributes(player):
    print()
    print('LIFE: ', player['player_life'] * '♥️ ', " | ", "POWER: ", player['player_power'] * '🥄')
    print()


def print_message(message=''):
    print(message)
