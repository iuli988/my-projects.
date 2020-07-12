import util
import dictionaries
import engine
import ui
import time
import players
import menu_start
import view
from art import text2art
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


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    # initial level
    level = 'BOARD_1'

    # initial key
    key = ''

    menu_start.run()

    ui.print_message('\n\n\n LEVEL %s \n\n\n' % (level[-1]))
    time.sleep(1.0)
    util.clear_screen()

    pass_key_input = False

    while level != 'WIN' and level != 'QUIT' and level != 'LOSE':

        util.clear_screen()
        pass_key_input = False

        view.print_table(players.data_to_print(dictionaries.player))

        # Set up board
        global BOARD_1
        global BOARD_2
        global BOARD_3
        # global items_u_will_use
        # global coordonate_of_items_that_u_will_use
        # player = create_player()
        BOARD_1 = engine.create_board()
        BOARD_2 = engine.create_board()
        BOARD_3 = engine.create_board()
        BOARD_1, items_u_will_use_1, coordonate_of_items_that_u_will_use_1 = engine.create_final_board(BOARD_1, little_boss_1)
        BOARD_2, items_u_will_use_2, coordonate_of_items_that_u_will_use_2 = engine.create_final_board(BOARD_2, little_boss_2)
        BOARD_3, items_u_will_use_3, coordonate_of_items_that_u_will_use_3 = engine.create_final_board(BOARD_3, boss)
        BOARD_1 = engine.create_board()
        BOARD_2 = engine.create_board()
        BOARD_3 = engine.create_board()
        util.clear_screen()
        is_running = True
        while is_running:
            print()
            print("U entered first level")
            print()
            items_u_will_use_1, coordonate_of_items_that_u_will_use_1 = engine.items_and_coordonates_that_u_can_use(BOARD_1)
            (BOARD_1, items_u_will_use, coordonate_of_items_that_u_will_use_1) = engine.create_final_board(BOARD_1, little_boss_1)
            (BOARD_1, items_u_will_use_1, coordonate_of_items_that_u_will_use_1) = engine.put_player_on_board(BOARD_1, little_boss_1)
            engine.move_something_and_gate(BOARD_1, player, little_boss_1, gate_1)

            if player['player_life'] > 0:
                print()
                print("U entered second level")
                print()
            items_u_will_use_2, coordonate_of_items_that_u_will_use_2 = engine.items_and_coordonates_that_u_can_use(BOARD_2)
            (BOARD_2, items_u_will_use_2, coordonate_of_items_that_u_will_use_2) = engine.create_final_board(BOARD_2, little_boss_2)
            engine.move_something_and_gate(BOARD_2, player, little_boss_2, gate_2)

            if player['player_life'] > 0:
                print()
                print("U entered the third level")
                print()
            items_u_will_use_3, coordonate_of_items_that_u_will_use_3 = engine.items_and_coordonates_that_u_can_use(BOARD_3)
            (BOARD_3, items_u_will_use_3, coordonate_of_items_that_u_will_use_3) = engine.create_final_board(BOARD_3, boss)
            engine.move_something_and_gate(BOARD_3, player, boss, gate_3)
            # ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        # elif key == 'i':
        #     print(inventory)
        is_running = False
        # util.clear_screen()
        print(key)
        # break
            # ui.display_board(board)

        key = util.key_pressed()
        # if key == 'q':
        #     is_running = False
        # elif key == 'i':
        #     print(inventory)

        # util.clear_screen()
        print(key)

        # Display essential info
        ui.print_player_essential_atributes(dictionaries.player)

        # Display board
        ui.display_board(board)

        # Message panel intoduction (always displayed)
        ui.print_message('  MESSAGE PANEL \n' + 17 * '-' + '\n')

        # Interaction whit items

        # Display inventory
        if key == 'i':
            ui.print_message('This is your inventory content: ')
            ui.print_table(dictionaries.inventory)

        # Interaction with other characters

        # Insert secret code
        if key == "c":
            engine.use_secret_code(dictionaries.player, dictionaries.others, level, dictionaries.codes)

        # Gate and level change handling
        # if engine.player_enters_gate() != level:
            # util.clear_screen()
            # level = engine.player_enters_gate()

            if level == 'BOARD_2' or level == 'BOARD_3':
                dictionaries.player['position_y'] = 15
                dictionaries.player['position_x'] = 3

            if level == 'WIN':
                pass_key_input = True
                pass
            else:
                ui.print_message('\n\n\n LEVEL %s \n\n\n' % (level[-1]))
                time.sleep(1.0)
                util.clear_screen()
                pass_key_input = True

        # Player input
        if pass_key_input is False:
            key = util.key_pressed()

        # Movement
        if pass_key_input is False:
            pass
        # engine.movement()

        # Check if quit
        if key == 'q':
            quit_assertion = ''
            while quit_assertion != 'y' and quit_assertion != 'n':
                util.clear_screen()
                print('Are you sure you want to quit? ( Y / N )')
                quit_assertion = util.key_pressed()
                if quit_assertion == 'y':
                    level = 'QUIT'
                elif quit_assertion == 'n':
                    pass
                else:
                    pass

        if dictionaries.player['player_life'] == 0:
            level = 'LOSE'

    if level == 'WIN':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("VICTORY!", font='block', chr_ignore=True))

    elif level == 'LOSE':
        util.clear_screen()
        ui.display_board(board)
        print(text2art("GAME OVER!", font='block', chr_ignore=True))
        time.sleep(10.7)

    print('\n\n\n Goodbye, see you soon!')
    time.sleep(1.0)


if __name__ == '__main__':
    main()
