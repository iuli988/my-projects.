import view
import sys
import players
from termcolor import colored
import util
import time
items_u_will_use = []

list_labels = ["Type", "Level of difficulty"]
list_options = {
                1: 'Start Play',
                2: 'Check instruction game',
                0: 'Exit'
}

choice_options = ['0', '1', '2']


def run():
    print(colored("\nMAIN MENU", 'yellow'))
    view.print_menu(list_options)
    print("\n")
    choice = input(str(colored('Your choice is: ', "green")))
    while choice in choice_options:
        if choice == '1':
            util.clear_screen()
            try:
                players.user_info(list_labels)
                break
            except Exception as error:
                print(str(error))
                time.sleep(3)
                continue
        elif choice == '2':
            view.print_instruction()
            print("\n")
            user_decision = input("If you want to come to main menu, please press 0 :")
            if user_decision == "0":
                util.clear_screen()
                run()
            else:
                print("try again")
        elif choice == '0':
            view.exit_message()
            sys.exit()
    else:
        print("Incorrect input. Try again, please!!!")
