import user_interface as ui
import csv
import model as md
import logger as lg
import colorama
from colorama import Fore, Back, Style

colorama.init()

lg.logging.info("Start")

def init():
    md.init_base()

def user_input(text=""):
    s = input(text)
    lg.logging.info("User entered: name = '" + s + "'")
    return s

def nul_menu(find_id=False):
    while True:
        print('0. Возврат в меню')
        choice_num = digit_check()
        if choice_num > 0 and find_id:
            return choice_num
        elif choice_num == 0:
            user_choice()
            return False
        

def choice_id():
    name = user_input("Введите часть имени, фамилии: ")
    res = md.find_contact(name)
    if res:
        print()
        [print(Fore.GREEN + f"{val}") for val in res]
        print(Style.RESET_ALL)
        print("Введите id сотрудника")
    else:
        sucess("По такому запросу результатов нет!", False)
    return str(nul_menu(True))

def sucess(text, ok):
    if not ok:
        lg.logging.info("Error: " + text)
        print(Fore.RED + f"\n{text}")
    else:
        lg.logging.info("Sucess: " + text)
        print(Fore.GREEN + f"\n{text}")
    print(Style.RESET_ALL)
    nul_menu()


def digit_check():
    try:
        input_number = user_input("Введите число:\n")
        return int(input_number)
    except ValueError:
        lg.logging.info("Error: Это должно быть число!")
        print(Fore.RED + "Это должно быть число!\n")
        print(Style.RESET_ALL)
        return digit_check()


def user_choice():
    ui.menu()
    choice_num = digit_check()
    if 0 > choice_num > 7:
        print('\nОшибка ввода!\n\Введите число!\n')
        user_choice()
    elif choice_num == 1:
        name = user_input("Введите Имя: ")
        second_name = user_input('Введите Фамилию: ')
        department = user_input('Введите Отдел: ')
        salary = user_input('Введите Зарплата: ')
        id = md.add_user(name, second_name, department, salary)
        if id > 0:
            sucess("Сотрудник id:" + str(id) + " принят!", True)
    elif choice_num == 2:
        id = choice_id()
        name = user_input("Новое Имя или пропустить - enter: ")
        second_name = user_input('Новая Фамилию или пропустить - enter: ')
        department = user_input('Новый Отдел или пропустить - enter: ')
        salary = user_input('Новая Зарплата или пропустить - enter: ')
        if md.update_user(id, {
            "name":name, 
            "second_name":second_name, 
            "department":department, 
            "salary":salary
        }):
            sucess("Сотрудник id:" + id + " обновлен!", True)
    elif choice_num == 3:
        name = user_input("Введите часть имени, фамилии или номера: ")
        res = md.find_contact(name)
        if res:
            print()
            [print(Fore.GREEN + f"{val}") for val in res]
            print(Style.RESET_ALL)
        else:
            sucess("Сотрудник не найден!", False)
        nul_menu()
    elif choice_num == 4:
        id = choice_id()
        if md.delete_user(id):
            sucess("Сотрудник id:" + id + " успешно уволен!", True)
    elif choice_num == 5:
        res = md.view_all_user()
        if res:
            print()
            [print(Fore.GREEN + f"{val}") for val in res]
            print(Style.RESET_ALL)
        else:
            sucess("Сотрудников нет в базе!", False)
        nul_menu()
    elif choice_num == 6:
        print("Для экспорта в файл export.txt нижмите enter")
        export_file = user_input("Иначе ведите путь до экспортируемого файла:")
        print("Для использования разделителя столбцов 'пробел' нижмите enter")
        separator = user_input("Иначе укажите разделитель столбцов:")
        if len(export_file) == 0:
            export_file = "export.txt"
        if len(separator) == 0:
            separator = " "

        data = md.view_all_user()
        with open(export_file, "w", encoding="UTF-8") as export:
            export.write("")
        for i in range(0, len(data)):
            with open(export_file, "a", encoding="UTF-8") as export:
                export.write(
                    str(data[i][0]) + separator 
                    + str(data[i][1]) + separator 
                    + str(data[i][2]) + separator 
                    + str(data[i][3]) + separator
                    + str(data[i][4])
                    + "\n"
                )
        sucess("Сотрудники успешно экспортированы в файл!", True)
    elif choice_num == 7:
        print("Для импорта из файла import.csv нижмите enter")
        inport_file = user_input("Иначе введите путь до импортируемого csv файла:")
        if len(inport_file) == 0:
            inport_file = "import.csv"

        with open(inport_file, "r", newline="", encoding="UTF-8") as csv_file:
            reader = csv.reader(csv_file)
            [md.add_user(val[0], val[1], val[2], val[3]) for val in reader]
        sucess("Сотрудники успешно импортированы", True)
    elif choice_num == 0:
        print(Fore.GREEN + '\nДо встречи!')
        exit()
