import user_interface as ui
import model as md

def init():
    md.init_base()

def nul_menu():
    print('0. Возврат в меню')
    choice_num = md.digit_check()
    if choice_num == 0 :
        user_choice()
    else:
        return choice_num

def user_choice():

    ui.menu()
    choice_num = md.digit_check()
    if 0 > choice_num > 9:
        print('\nОшибка ввода!\n\Введите число!\n')
        user_choice()
    elif choice_num == 1:
        md.create_json()
    elif choice_num == 2:
        md.add_to_json()
    elif choice_num == 3:
        md.change_phone_number()
    elif choice_num == 4:
        md.change_surname()
    elif choice_num == 5:
        md.find_contact(True)
    elif choice_num == 6:
        md.delete_contact()
    elif choice_num == 7:
        md.view_all_contacts()
    elif choice_num == 8:
        md.export_txt()
    elif choice_num == 9:
        md.import_csv()
    elif choice_num == 0:
        print('До встречи!')
        exit()
