import json
import csv
import os.path
import controller as controller
import colorama
from colorama import Fore, Back, Style
import logger as lg

colorama.init()

lg.logging.info("Start")

path_to_db = "db.json"

def init_base():
    if not os.path.exists(path_to_db):
        json_data = []
        with open(path_to_db, "w") as file:
            file.write(json.dumps(json_data, indent=2, ensure_ascii=False))

def create_json():
    json_data = []
    with open(path_to_db, "w") as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    sucess("Пустой файл базы данных создан!", True)


def add_to_json():
    with open(path_to_db, encoding='UTF-8') as fh:
        data = json.load(fh)    
    next_id = int(data[-1]["id"]) + 1 if data else 1
    name = input("Введите имя: ")
    lg.logging.info("User entered: name = '" + name + "'")
    second_name = input('Введите Фамилию: ')
    lg.logging.info("User entered: second_name = '" + second_name + "'")
    phone = input('Введите номер телефона: ')
    lg.logging.info("User entered: phone = '" + phone + "'")
    json_data = {
        "id": str(next_id),
        "name": name,
        "second_name": second_name,
        "phone": phone
    }
    data.append(json_data)
    with open(path_to_db, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print() 
    sucess(f"Новый контакт с id:{next_id} добавлен!", True)


def change_phone_number():  
    find_contact()
    print("Введите id контакта")
    id = str(controller.nul_menu())
    lg.logging.info("User entered: id = '" + id + "'")
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if id == data[i]["id"]:
                phone = input("Новый номер: ")
                data[i]["phone"] = phone
                lg.logging.info("User entered: phone = '" + phone + "'")
    with open(path_to_db, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
    sucess("Номер успешно изменён!", True)


def change_surname():
    find_contact()
    print("Введите id контакта")
    id = str(controller.nul_menu())
    lg.logging.info("User entered: id = '" + id + "'")
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if id == data[i]["id"]:
                second_name = input("Новая фамилия: ")
                data[i]['second_name'] = second_name
                lg.logging.info("User entered: second_name = '" + second_name + "'")
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    sucess("Фамилия успешно изменена!", True)

def delete_contact():
    find_contact()
    print("Введите id контакта")
    id = str(controller.nul_menu())
    lg.logging.info("User entered: id = '" + id + "'")
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if id == data[i]["id"]:
                del data[i]
    with open(path_to_db, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
    sucess("Контакт успешно удалён!", True)


def find_contact(only_find):
    name = input("Введите часть имени, фамилии или номера: ")
    lg.logging.info("User entered: name = '" + name + "'")
    if_found = False
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if (
                data[i]["name"].lower().find(name.lower()) != -1 
                or data[i]["second_name"].lower().find(name.lower()) != -1
            ):
                print(data[i])
                if_found = True
        print()
        if not if_found:
            sucess("По такому запросу результатов нет!", False)
    if only_find:
        controller.nul_menu()  

def view_all_contacts():
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    print()
    controller.nul_menu()


def export_txt():
    print("Для экспорта в файл export.txt нижмите enter")
    export_file = input("Иначе ведите путь до экспортируемого файла:\n")
    print("Для использования разделителя столбцов 'пробел' нижмите enter")
    separator = input("Иначе укажите разделитель столбцов:\n")
    
    if len(export_file) == 0:
        export_file = "export.txt"
    with open(export_file, "w", encoding="UTF-8") as export:
        export.write("")
    if len(separator) == 0:
        separator = " "
    lg.logging.info("User entered: export_file = '" + export_file + "'")
    lg.logging.info("User entered: separator = '" + separator + "'")
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open(export_file, "a", encoding="UTF-8") as export:
                export.write(data[i]["id"] + separator + data[i]["name"] + separator + 
                data[i]["second_name"] + separator + data[i]["phone"] + "\n")

    sucess("Контакты успешно экспортированы в файл!", True)

def import_csv():
    print("Для импорта из файла import.csv нижмите enter")
    inport_file = input("Иначе введите путь до импортируемого csv файла:")
    if len(inport_file) == 0:
        inport_file = "import.csv"
    lg.logging.info("User entered: inport_file = " + inport_file)
    with open(inport_file, "r", newline="", encoding="UTF-8") as csv_file:
        reader = csv.reader(csv_file)
        with open(path_to_db, encoding='utf-8') as fh:
            data = json.load(fh)
        next_id = int(data[-1]["id"]) + 1 if data else 1
        for row in reader:
            name, second_name, phone = row[0], row[1], row[2]
            json_data = {
                "id": str(next_id),
                "name": name,
                "second_name": second_name,
                "phone": phone
            }
            data.append(json_data)
            next_id += 1
        
        with open(path_to_db, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    sucess("Контакты успешно импортированы", True)


def digit_check():
    try:
        input_number = input("Введите число:\n")
        lg.logging.info("The user has selected item number '" + input_number + "'")
        return int(input_number)
    except ValueError:
        lg.logging.info(f"Error: Это должно быть число!")
        print(Fore.RED + "Это должно быть число!\n")
        print(Style.RESET_ALL)
        return digit_check()


def sucess(text, ok):
    if not ok:
        lg.logging.info("Error: " + text)
        print(Fore.RED + f"{text}")
    else:
        lg.logging.info("Sucess: " + text)
        print(Fore.GREEN + f"{text}")
    print(Style.RESET_ALL)
    controller.nul_menu()