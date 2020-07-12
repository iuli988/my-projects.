from model.sales import sales
from view import terminal as view
from model import data_manager
import random
import string
import datetime
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


def list_transactions():
    result = []
    result.append(sales.HEADERS)
    with open(sales.DATAFILE) as f:
        for line in f:
            result.append(line.strip().split(';'))
    view.print_table(result)


def date_of_transaction():
    number_days_list = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    now = datetime.datetime.now()

    while True:
        transaction_year = input("Enter year of transaction (YYYY): ")

        try:
            transaction_year = int(transaction_year)

            if transaction_year in range(1900, now.year + 1):
                break

        except ValueError:
            print("The inserted value isn' satisfying :D")

    if transaction_year % 4 == 0:
        number_days_list[1] = 29

    else:
        number_days_list[1] = 28

    while True:
        transaction_month = input("Enter month of transaction (MM): ")

        try:
            transaction_month = int(transaction_month)

            if transaction_month in range(1, 13):
                break

        except ValueError:
            print("The inserted value isn't satisfying :D")

    while True:
        transaction_day = input("Enter day of transaction (DD): ")

        try:
            transaction_day = int(transaction_day)

            if transaction_day in range(1, number_days_list[transaction_month - 1] + 1):
                break

        except:
            print("The inserted value isn't satisfying :D"
                  "must be an integer")

    x = str(transaction_year) + "/" + str(transaction_month) + "/" + str(transaction_day)
    return x


def get_info_transaction():
    transaction = []

    n = generate_id()
    m = generate_id()
    transaction.append(n)
    transaction.append(m)

    transaction.append(input("Enter the name of the product: "))

    while True:
        price = input("Insert price:")

        try:
            price = float(price)
            break

        except ValueError:
            print("The insertet alue is nt number")

    transaction.append(str(price))
    date = date_of_transaction()
    transaction.append(date)

    return transaction


def add_transaction():
    a = get_info_transaction()
    with open(sales.DATAFILE, "a") as f:
        f.write("\n" + ";".join(a))
    list_transactions()


def update_transaction():
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated.')
    with open(sales.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                user_update = input('Enter the new input:')
                list_of_file_lines[i] = list(
                    user_update.strip().split(';'))
                break
    with open(sales.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')


def delete_transaction():
    list_transactions()
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated.')
    with open(sales.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                list_of_file_lines.remove(list_of_file_lines[i])
                break
    with open(sales.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')
    list_transactions()


def get_biggest_revenue_product():
    dic_of_file_lines_2 = {}
    max_element = 0
    element_2 = "element"
    with open(sales.DATAFILE, 'r+') as f:

        for line in f:
            words = line.strip().split(';')

            if words[2] in dic_of_file_lines_2:
                dic_of_file_lines_2[words[2]] += float(words[3])
                if max_element < dic_of_file_lines_2[words[2]]:
                    max_element = dic_of_file_lines_2[words[2]]
                    element_2 = words[2]

            else:
                dic_of_file_lines_2[words[2]] = float(words[3])
                if max_element < dic_of_file_lines_2[words[2]]:
                    max_element = dic_of_file_lines_2[words[2]]
                    element_2 = words[2]
    print(str(element_2) + ": " + str(max_element))


def get_biggest_revenue_transaction():
    name_0f_product_list = []
    maxim = 0.0
    with open(sales.DATAFILE, 'r') as f:

        for line in f:
            name_0f_product_list.append(line.strip().split(';'))

    for i in range(len(name_0f_product_list)):

        if maxim < float(name_0f_product_list[i][3]):
            maxim = float(name_0f_product_list[i][3])
            list_good = []
            list_good.append(name_0f_product_list[i][1])
            list_good.append(name_0f_product_list[i][2])
            list_good.append(name_0f_product_list[i][3])
            list_good.append(name_0f_product_list[i][4])
    print(list_good)


def count_transactions_between():
    my_list = data_manager.read_table_from_file(sales.DATAFILE, ";")
    list_with_years = []
    list_with_months = []
    list_with_days = []
    year_start_input = int(input("The year from which the transactions begin: "))
    while year_start_input not in range(1990, 2021):
        year_start_input = int(input("The year from which the transactions begin(1990-2020): "))

    mounth_start_input = int(input("The mounth from which the transactions begin: "))
    while mounth_start_input not in range(1, 13):
        mounth_start_input = int(input("The mounth from which the transactions begin(1-12): "))

    day_start_input = int(input("The day from which the transactions begin: "))
    while day_start_input not in range(1, 32):
        day_start_input = int(input("The day from which the transactions begin(1-31): "))

    year_finish_input = int(input("In what year does the transaction end?: "))
    while year_finish_input not in range(1990, 2021):
        year_finish_input = int(input("In what year does the transaction end?(1990-2020): "))

    mounth_finish_input = int(input("In what mounth does the transaction end?: "))
    while mounth_finish_input not in range(1, 13):
        mounth_finish_input = int(input("In what mounth does the transaction end?(1-12): "))

    day_finish_input = int(input("In what day does the transaction end?: "))
    while day_finish_input not in range(1, 32):
        day_finish_input = int(input("In what day does the transaction end?(1-31): "))

    for element in my_list:
        date = element[4][:4]
        if int(date) >= year_start_input and int(date) <= year_finish_input:
            list_with_years.append(element)

    for element1 in list_with_years:
        date11 = element1[4][:4]
        date22 = element1[4][5:7]

        if int(date11) == year_start_input:
            if int(date22) >= mounth_start_input and int(date22) <= mounth_finish_input:
                list_with_months.append(element1)

        else:
            list_with_months.append(element1)

    for element2 in list_with_months:
        date33 = element[4][5:7]
        date44 = element2[4][8:10]
        if int(date33) == mounth_start_input:
            if int(date44) >= day_start_input and int(date44) <= day_finish_input:
                list_with_days.append(element2)

        else:
            list_with_days.append(element2)

    print("The number of transactions: " + str(len(list_with_days)))


def sum_transactions_between():
    my_list = data_manager.read_table_from_file(sales.DATAFILE, ";")
    list_with_years = []
    list_with_months = []
    list_with_days = []
    sumaL = 0
    year_start_input = int(input("The year from which the transactions begin: "))
    while year_start_input not in range(1990, 2021):
        year_start_input = int(input("The year from which the transactions begin(1990-2020): "))

    mounth_start_input = int(input("The mounth from which the transactions begin: "))
    while mounth_start_input not in range(1, 13):
        mounth_start_input = int(input("The mounth from which the transactions begin(1-12): "))

    day_start_input = int(input("The day from which the transactions begin: "))
    while day_start_input not in range(1, 32):
        day_start_input = int(input("The day from which the transactions begin(1-31): "))

    year_finish_input = int(input("In what year does the transaction end?: "))
    while year_finish_input not in range(1990, 2021):
        year_finish_input = int(input("In what year does the transaction end?(1990-2020): "))

    mounth_finish_input = int(input("In what mounth does the transaction end?: "))
    while mounth_finish_input not in range(1, 13):
        mounth_finish_input = int(input("In what mounth does the transaction end?(1-12): "))

    day_finish_input = int(input("In what day does the transaction end?: "))
    while day_finish_input not in range(1, 32):
        day_finish_input = int(input("In what day does the transaction end?(1-31): "))

    for element in my_list:
        date = element[4][:4]
        if int(date) >= year_start_input and int(date) <= year_finish_input:
            list_with_years.append(element)

    for element1 in list_with_years:
        date11 = element1[4][:4]
        date22 = element1[4][5:7]

        if int(date11) == year_start_input:
            if int(date22) >= mounth_start_input and int(date22) <= mounth_finish_input:
                list_with_months.append(element1)

        else:
            list_with_months.append(element1)

    for element2 in list_with_months:
        date33 = element[4][5:7]
        date44 = element2[4][8:10]
        if int(date33) == mounth_start_input:
            if int(date44) >= day_start_input and int(date44) <= day_finish_input:
                list_with_days.append(element2)

        else:
            list_with_days.append(element2)

    for element in list_with_days:
        suma = element[3]
        sumaL += float(suma)

    print("Sum of transactions: " + str(sumaL))


def run_operation(option):
    if option == '1':
        os.system('clear')
        list_transactions()
    elif option == '2':
        os.system('clear')
        add_transaction()
    elif option == '3':
        os.system('clear')
        update_transaction()
    elif option == '4':
        os.system('clear')
        delete_transaction()
    elif option == '5':
        os.system('clear')
        get_biggest_revenue_transaction()
    elif option == '6':
        os.system('clear')
        get_biggest_revenue_product()
    elif option == '7':
        os.system('clear')
        count_transactions_between()
    elif option == '8':
        os.system('clear')
        sum_transactions_between()
    elif option == '9':
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between",
               "Back to main menu"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '9':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(operation)
        except KeyError as err:
            view.print_error_message(err)
