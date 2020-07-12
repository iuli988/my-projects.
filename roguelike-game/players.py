import dictionaries
from termcolor import colored


BOARD_WIDTH = 80
BOARD_HEIGHT = 20

list_labels = ["Type", "Level of difficulty"]

game_player = {'race': ['1', '2', '3'],
               'Level_of_difficulty': ['1', '2', '3'], }


def user_info(list_labels):
    print("\nYou can choose who you want to be :D \nYour options: (1)Man, (2) or (3)Adolescent\n")

    for elem in range(len(list_labels)):
        user_answer = input(str(list_labels[elem])+" : ")
        if elem == 0:
            if user_answer not in game_player['race']:
                raise Exception(colored("It's not acceptable choice. Try again\n", "red"))
            else:
                if user_answer == '1':
                    print(colored("You are a Man so you are more powerful than you think", 'magenta'))
                    dictionaries.player['player_power'] = 5
                elif user_answer == '2':
                    print(colored("You chose ... and you get ... :D!!!It can be useful later", 'magenta'))
                    dictionaries.player['additional_elements'] = ''
                elif user_answer == '3':
                    print(colored("Hello little boy ;) Because you're still a child, You get a more life_points ", 'magenta'))
                    dictionaries.player['player_life'] = 2
                print("\nOptions: (1) Easy, (2) Medium, (3) Hard \n")
        elif elem == 1:
            if user_answer not in game_player['Level_of_difficulty']:
                raise Exception(colored("You choose only (1)Easy ,(2) Medium or (3)Hard level of difficulty\n", "red"))
            else:
                if user_answer == '1':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 5
                elif user_answer == '2':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 3
                elif user_answer == '3':
                    dictionaries.player['player_life'] = dictionaries.player['player_life'] + 1

        dictionaries.player[list_labels[elem]] = user_answer


def data_to_print(data):
    keys = ["Type", "Level of difficulty"]
    data_print = {key: dictionaries.player[key] for key in keys}
    for key in data_print:
        if key == "Type":
            if data_print[key] == '1':
                data_print[key] = 'Man'
            elif data_print[key] == '2':
                data_print[key] = '...'
            else:
                data_print[key] = 'Adolescent'
        elif key == "Level of difficulty":
            if data_print[key] == '1':
                data_print[key] = 'Easy'
            elif data_print[key] == '2':
                data_print[key] = 'Medium'
            else:
                data_print[key] = 'Hard'
    return data_print
