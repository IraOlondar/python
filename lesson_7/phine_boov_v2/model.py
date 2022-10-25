import json
import csv
import os.path
import configuration as cf

path_to_db = cf.db_name


def init_base():
    if not os.path.exists(path_to_db):
        json_data = []
        with open(path_to_db, "w") as file:
            file.write(json.dumps(json_data, indent=2, ensure_ascii=False))

def create_json():
    json_data = []
    with open(path_to_db, "w") as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    return True


def add_to_json(name, second_name, phone):
    with open(path_to_db, encoding='UTF-8') as fh:
        data = json.load(fh)    
    next_id = int(data[-1]["id"]) + 1 if data else 1
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
    return next_id


def change_phone_number(id, phone):  
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if id == data[i]["id"]:
                phone = input("Новый номер: ")
                data[i]["phone"] = phone
    with open(path_to_db, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
    return True


def change_surname(id, second_name):
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if id == data[i]["id"]:
                data[i]['second_name'] = second_name
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    return True

def delete_contact(id):
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if id == data[i]["id"]:
                del data[i]
                break
    with open(path_to_db, "w", encoding="UTF-8") as file:
        json.dump(data, file, indent=4)
    return True


def find_contact(name):
    if_found = False
    a = []
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if (
                data[i]["name"].lower().find(name.lower()) != -1 
                or data[i]["second_name"].lower().find(name.lower()) != -1
            ):
                a.append(data[i])
                if_found = True

        if not if_found:
            return False

        return a


def view_all_contacts():
    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    print()


def export_txt(export_file, separator):
    
    with open(export_file, "w", encoding="UTF-8") as export:
        export.write("")

    with open(path_to_db, "r", encoding="UTF-8") as file:
        data = json.load(file)
        for i in range(0, len(data)):
            with open(export_file, "a", encoding="UTF-8") as export:
                export.write(data[i]["id"] + separator + data[i]["name"] + separator + 
                data[i]["second_name"] + separator + data[i]["phone"] + "\n")

    return True

def import_csv(inport_file):
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

    return True
