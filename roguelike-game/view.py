from termcolor import colored


def print_menu(list_options):
    index = 1
    for key in list_options:
        if key != 0:
            print("(", index, ")", list_options[key])
            index += 1
    print("( 0 )", list_options[0])


def print_table(data):
    index = 0
    print("-" * 40)
    for key in data:
        if index == 0:
            print(colored(key.ljust(int(len("Level of difficulty"))), "cyan"), ":", colored(data[key], "cyan"))
        else:
            print(colored(key.ljust(int(len("Level of difficulty"))), "cyan"), ":", colored(data[key], "cyan"))
        index += 1
    print("-" * 40)


def print_instruction():

    print(colored("Start? :\n", 'cyan', attrs=['bold', 'underline']))
    print('\n')
    print("Play")
    print('\n')
    print("Use W to go up")
    print("Use S to go down")
    print("Use D to go right")
    print("Use A to go left")
    print('\n')


def exit_message():
    print('Goodbye!')
