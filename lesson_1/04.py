#Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

def input_quarter():
    not_error = True
    while not_error:
        try:
            number = int(input(f"Номер координатной четверти (1-4) = "))
            if 1 <= number <= 4:
                not_error = False
                a = number
            else:
    
                not_error = True
                print("Это не номер четверти!\nПопробуйте еше раз")       
        except ValueError:
            print("Введено не число!\nПопробуйте еше раз")
    return a

def check_coord(quarter):
    text = "X > 0, Y < 0"
    if quarter == 1:
        text = "X > 0, Y > 0"
    elif quarter == 2:
        text = "X < 0, Y > 0"
    elif quarter == 2:
        text = "X < 0, Y < 0"
    print(f"Диаразон координат {quarter} четверти: {text}")

check_coord(input_quarter())