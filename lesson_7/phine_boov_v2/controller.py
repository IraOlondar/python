import user_interface as ui
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
    name = user_input("Введите часть имени, фамилии или номера: ")
    res = md.find_contact(name)
    if res:
        [print(val) for val in res]
        print("\nВведите id контакта")
    else:
        sucess("По такому запросу результатов нет!", False)
    return str(nul_menu(True))

def sucess(text, ok):
    if not ok:
        lg.logging.info("Error: " + text)
        print(Fore.RED + f"{text}")
    else:
        lg.logging.info("Sucess: " + text)
        print(Fore.GREEN + f"{text}")
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
    if 0 > choice_num > 9:
        print('\nОшибка ввода!\n\Введите число!\n')
        user_choice()
    elif choice_num == 1:
        if md.create_json():
            sucess("Пустой файл базы данных создан!", True)
    elif choice_num == 2:
        name = user_input("Введите имя: ")
        second_name = user_input('Введите Фамилию: ')
        phone = user_input('Введите номер телефона: ')
        id = md.add_to_json(name, second_name, phone)
        if int(id) > 0:
            sucess("Контакт id:" + id + " добавлен!", True)
    elif choice_num == 3:
        id = choice_id()
        phone = user_input("Новый номер: ")
        if md.change_phone_number(id, phone):
            sucess("Контакт id:" + id + " обновлен!", True)
    elif choice_num == 4:
        id = choice_id()
        second_name = user_input("Новая фамилия: ")
        if md.change_surname(id, second_name):
            sucess("Контакт id:" + id + " обновлен!", True)
    elif choice_num == 5:
        name = user_input("Введите часть имени, фамилии или номера: ")
        res = md.find_contact(name)
        if res:
            [print(val) for val in res]
        else:
            sucess("Контакт не найден!", False)
        print()
        nul_menu()
    elif choice_num == 6:
        id = choice_id()
        if md.delete_contact(id):
            sucess("Контакт id:" + id + " успешно удалён!", True)
    elif choice_num == 7:
        md.view_all_contacts()
        nul_menu()
    elif choice_num == 8:
        print("Для экспорта в файл export.txt нижмите enter")
        export_file = user_input("Иначе ведите путь до экспортируемого файла:\n")
        print("Для использования разделителя столбцов 'пробел' нижмите enter")
        separator = user_input("Иначе укажите разделитель столбцов:\n")

        if len(export_file) == 0:
            export_file = "export.txt"

        if len(separator) == 0:
            separator = " "

        if md.export_txt(export_file, separator):
            sucess("Контакты успешно экспортированы в файл!", True)
    elif choice_num == 9:
        print("Для импорта из файла import.csv нижмите enter")
        inport_file = user_input("Иначе введите путь до импортируемого csv файла:")
        if len(inport_file) == 0:
            inport_file = "import.csv"
        
        if md.import_csv(inport_file):
            sucess("Контакты успешно импортированы", True)
    elif choice_num == 0:
        print('До встречи!')
        exit()
