from view import terminal as view
from controller import crm_controller, sales_controller, hr_controller
import os


def load_module(option):
    if option == '1':
        os.system('clear')
        crm_controller.menu()
    elif option == '2':
        os.system('clear')
        hr_controller.menu()
    elif option == '3':
        os.system('clear')
        sales_controller.menu()
    elif option == '4':
        return 4
    else:
        raise KeyError()


def display_menu():
    options = ["Customer Relationship Management (CRM)",
               "Sales",
               "Human Resources",
               "Exit program"]
    view.print_menu("Main menu", options)


def menu():
    option = None
    while option != '4':
        # display_menu()
        try:
            option = view.get_input("Select module: ")
            load_module(option)
        except KeyError:
            view.print_error_message("There is no such option!")
        except ValueError:
            view.print_error_message("Please enter a number!")
    view.print_message("Good-bye!")
