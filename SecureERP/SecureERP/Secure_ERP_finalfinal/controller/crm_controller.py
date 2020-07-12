from model.crm import crm
from view import terminal as view
import random
import string
import re
import os
from view import terminal


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_specialchars=r"+-!"):

    myId = []
    for small_letter in range(number_of_small_letters):
        myId.append(random.choice(string.ascii_lowercase))
    for capital_letter in range(number_of_capital_letters):
        myId.append(random.choice(string.ascii_uppercase))
    for digit in range(number_of_digits):
        myId.append(str(random.randint(1, 10)))
    for special_char in range(number_of_special_chars):
        myId.append(random.choice(allowed_specialchars))
    random.shuffle(myId)
    return ''.join(myId)


def list_customers():
    result = []
    result.append(crm.HEADERS)
    with open(crm.DATAFILE, 'r') as f:
        for line in f:
            result.append(line.strip().split(';'))
    # return result
    view.print_table(result)


def add_customer():
    regex = '^\w+([.-]?\w+)@\w+([.-]?\w+)(.\w{2,3})+$'
    customers = []
    n = generate_id()
    customers.append(n)
    customers.append(input("Enter your name: "))

    valid_email = input("Enter your email adress: ")

    while len(customers) == 2:

        if(re.search(regex, valid_email)):
            customers.append(valid_email)

        else:
            print("Invalid Email")
            valid_email = input("Enter your email adress: ")

    sub_input = int(input("Enter your sub(0 for YES, 1 for NO: "))
    lista = [0, 1]
    while True:
        if sub_input not in lista:
            sub_input = int(input("Enter your sub(0 for YES, 1 for NO: "))
        else:
            break

    customers.append(str(sub_input))

    with open(crm.DATAFILE, "a") as f:
        f.write("\n" + ";".join(customers))

    list_customers()


def update_customer():
    list_customers()
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated: ')
    with open(crm.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                user_update = input('Enter the new input:')
                list_of_file_lines[i] = list(
                    user_update.strip().split(';'))
                break
    with open(crm.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')
    list_customers()


def delete_customer():
    list_customers()
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated: ')
    with open(crm.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                list_of_file_lines.remove(list_of_file_lines[i])
                break
    with open(crm.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')
    list_customers()


def get_subscribed_emails():
    emails = []
    subscribed_emails = []
    with open(crm.DATAFILE, 'r+') as f:
        for line in f:
            emails.append(line.strip().split(';'))
    for i in range(len(emails)):
        if emails[i][3] == "1":
            subscribed_emails.append(emails[i][2])
    print(subscribed_emails)


def run_operation(option):
    if option == '1':
        os.system('clear')
        list_customers()
    elif option == '2':
        os.system('clear')
        add_customer()
    elif option == '3':
        os.system('clear')
        update_customer()
    elif option == '4':
        os.system('clear')
        delete_customer()
    elif option == '5':
        os.system('clear')
        get_subscribed_emails()
    elif option == '6':
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails",
               "Back to main menu"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '6':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(operation)
        except KeyError as err:
            view.print_error_message(err)
