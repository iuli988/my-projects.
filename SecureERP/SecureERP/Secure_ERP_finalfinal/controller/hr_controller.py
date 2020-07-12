from model.hr import hr
from view import terminal as view
from model import data_manager
import string
import random
import datetime
import os
from datetime import date
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


def list_employees():
    result = []
    result.append(hr.HEADERS)
    with open(hr.DATAFILE) as f:
        for line in f:
            result.append(line.strip().split(';'))
    view.print_table(result)


def add_employee():
    employeers = []
    ids = generate_id()
    employeers.append(ids)
    employeers.append(input(str(("Enter your name: "))))
    birthday = ""
    birth_year = int(input("Enter year of birth(YYYY): "))
    while True:
        try:
            if birth_year in range(1920, 2003):
                birthday += str(birth_year) + "-"
                break

            else:
                birth_year = int(input("Enter year of birth(YYYY): "))
        except ValueError:
            birth_month = int(input("Enter your birth month(MM): "))

    birth_month = int(input("Enter your birth month(MM): "))
    while True:
        try:
            if birth_month in range(1, 13):
                if len(str(birth_month)) < 2:
                    birthday += "0" + str(birth_month) + "-"

                else:
                    birthday += str(birth_month) + "-"
                break

            else:
                birth_month = int(input("Enter your birth month(MM): "))
        except ValueError:
            birth_month = int(input("Enter your birth month(MM): "))

    birth_day = int(input("Enter your birthday(ZZ): "))
    while True:
        try:
            if birth_day in range(1, 32):
                if len(str(birth_day)) < 2:
                    birthday += "0" + str(birth_day)

                else:

                    birthday += str(birth_day)
                break

            else:
                birth_day = int(input("Enter your birthday(ZZ): "))
        except ValueError:
            birth_day = int(input("Enter your birthday(ZZ): "))

    employeers.append(birthday)

    departments = ["sales", "production", "purchasing", "marketing"]
    department = str(input("What is your department?: "))
    while department not in departments:
        print("These are the departments: sales, production, purchasing, marketing.")
        department = str(input("What is your department?: "))

    employeers.append(department)

    clearance = int(input("Enter your clearance level(0/7): "))
    while True:
        if clearance in range(0, 8):
            employeers.append(str(clearance))
            break
        else:
            clearance = int(input("Enter your clearance level(0/7): "))

    with open(hr.DATAFILE, "a") as f:
        f.write("\n" + ";".join(employeers))
    list_employees()


def update_employee():
    list_employees()
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated: ')
    with open(hr.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                user_update = input('Enter the new input:')
                list_of_file_lines[i] = list(
                    user_update.strip().split(';'))
                break
    with open(hr.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')
    list_employees()


def delete_employee():
    list_employees()
    list_of_file_lines = []
    id_to_be_updated = input('Please enter an ID to be updated: ')
    with open(hr.DATAFILE, 'r+') as f:
        for line in f:
            list_of_file_lines.append(line.strip().split(';'))
        for i in range(len(list_of_file_lines)):
            if list_of_file_lines[i][0] == id_to_be_updated:
                list_of_file_lines.remove(list_of_file_lines[i])
                break
    with open(hr.DATAFILE, 'w') as f:
        for index, i in enumerate(list_of_file_lines):
            if index == len(list_of_file_lines)-1:
                f.write(';'.join(i))
            else:
                f.write(';'.join(i) + '\n')
    list_employees()


def get_oldest_and_youngest():
    read_file = data_manager.read_table_from_file(hr.DATAFILE, ';')

    biggest_year = 0
    smallest_year = 3000

    biggest_mounth = 0
    smallest_mounth = 3000

    biggest_day = 0
    smallest_day = 3000

    the_youngest = []
    the_oldest = []

    the_youngestM = []
    the_oldestM = []

    the_youngestD = []
    the_oldestD = []

    year_result = []
    year_resultO = []

    mounth_result = []
    mounth_resultO = []

    day_result = []
    day_resultO = []

    for date in read_file:
        year = date[2][:4]
        if int(year) <= smallest_year:
            smallest_year = int(year)
            the_oldest.append(date)

    for result in the_oldest:
        rezultat = result[2][:4]
        if int(rezultat) == smallest_year:
            year_resultO.append(result)

    for dateM in year_resultO:
        mounth = dateM[2][5:7]
        if int(mounth) <= smallest_mounth:
            smallest_mounth = int(mounth)
            the_oldestM.append(dateM)

    for result1 in the_oldestM:
        rezultat1 = result1[2][5:7]
        if int(rezultat1) == smallest_mounth:
            mounth_resultO.append(result1)

    for dateD in mounth_resultO:
        day = dateD[2][8:10]
        if int(day) <= smallest_day:
            smallest_day = int(day)
            the_oldestD.append(dateD)

    for result2 in the_oldestD:
        rezultat2 = result2[2][8:10]
        if int(rezultat2) == smallest_day:
            day_resultO.append(result2)

    print("The oldest employee is: " + day_resultO[0][1])

    for date in read_file:
        year = date[2][:4]
        if int(year) >= biggest_year:
            biggest_year = int(year)
            the_youngest.append(date)

    for result in the_youngest:
        rezultat = result[2][:4]
        if int(rezultat) == biggest_year:
            year_result.append(result)

    for dateM in year_result:
        mounth = dateM[2][5:7]
        if int(mounth) >= biggest_mounth:
            biggest_mounth = int(mounth)
            the_youngestM.append(dateM)

    for result1 in the_youngestM:
        rezultat1 = result1[2][5:7]
        if int(rezultat1) == biggest_mounth:
            mounth_result.append(result1)

    for dateD in mounth_result:
        day = dateD[2][8:10]
        if int(day) >= biggest_day:
            biggest_day = int(day)
            the_youngestD.append(dateD)

    for result2 in the_youngestD:
        rezultat2 = result2[2][8:10]
        if int(rezultat2) == biggest_day:
            day_result.append(result2)

    print("The youngest employee is: " + day_result[0][1])


def get_average_age():
    data = []
    date_of_birth = []
    ages_in_days = []
    ages = []
    with open(hr.DATAFILE, "r") as f:
        for line in f:
            data.append(line.strip().split(';'))
    for line in data:
        date_of_birth.append(line[2])
    for i in date_of_birth:
        datetimeFormat = '%Y-%m-%d'
        date1 = '2020-04-03'
        date2 = i
        diff = datetime.datetime.strptime(date1, datetimeFormat).date()\
            - datetime.datetime.strptime(date2, datetimeFormat).date()
        ages_in_days.append(str(diff).split())
    for i in ages_in_days:
        year = int(i[0]) / 365
        ages.append(year)
    avg = sum(ages)/len(ages)
    print("The average age is ", round(avg, 2))


def next_birthdays(date_str):
    list_employees()
    dic = {}
    names = []
    data_file = hr.DATAFILE
    for line in data_file[1:]:
        dic.update({line[1]: line[2]})
    for key, value in dic.items():
        new_value = date_str[0:5] + value[5:]
        start_date = date.datetime.strptime(date_str, '%Y-%m-%d').date()
        end_date = date.datetime.strptime(new_value, '%Y-%m-%d').date()
        delta = (end_date - start_date).days
        if delta > 0 and delta <= 14:
            names.append(key)
    view.print_general_results(
        names, f'Birthdays in the next two weeks {date_str}')


def count_employees_with_clearance():
    dic_of_file_lines_2 = {}

    with open(hr.DATAFILE, 'r') as f:

        for line in f:
            words = line.strip().split(';')
            if words[4] in dic_of_file_lines_2:
                dic_of_file_lines_2[words[4]] += 1
            else:
                dic_of_file_lines_2[words[4]] = 1

    print(dic_of_file_lines_2)


def count_employees_per_department():
    dic_of_file_lines_2 = {}

    with open(hr.DATAFILE, 'r') as f:

        for line in f:
            words = line.strip().split(';')
            if words[3] in dic_of_file_lines_2:
                dic_of_file_lines_2[words[3]] += 1
            else:
                dic_of_file_lines_2[words[3]] = 1

    print(dic_of_file_lines_2)


def run_operation(option):
    if option == '1':
        os.system('clear')
        list_employees()
    elif option == '2':
        os.system('clear')
        add_employee()
    elif option == '3':
        os.system('clear')
        update_employee()
    elif option == '4':
        os.system('clear')
        delete_employee()
    elif option == '5':
        os.system('clear')
        get_oldest_and_youngest()
    elif option == '6':
        os.system('clear')
        get_average_age()
    elif option == '7':
        os.system('clear')
        next_birthdays(view.get_input('Type starting date (yyyy-mm-dd): '))
    elif option == '8':
        os.system('clear')
        count_employees_with_clearance()
    elif option == '9':
        os.system('clear')
        count_employees_per_department()
    elif option == '0':
        return 0
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department",
               "Back to main menu"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation: ")
            run_operation(operation)
        except KeyError as err:
            view.print_error_message(err)
