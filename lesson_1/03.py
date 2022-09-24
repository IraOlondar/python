#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
# находится эта точка (или на какой оси она находится). 

def input_coord():
    name = ["X", "Y"]
    arr = []
    for i, nam in enumerate(name):
        not_nul = False
        while not not_nul:
            try:
                number = float(input(f"{nam} = "))
                print(f"{number} {i}")
                if number == 0:
                    not_nul = False
                    print("Координата не должно быть равна 0") 
                else:
                    not_nul = True
                    arr.append(number)          
            except ValueError:
                print("Введено не число!")
    return arr

def check_quarter(point):
    text = 4
    if point[0] > 0 and point[1] > 0:
        text = 1
    elif point[0] < 0 and point[1] > 0:
        text = 2
    elif point[0] < 0 and point[1] < 0:
        text = 3
    print(f"Точка находится в {text} четверти")

check_quarter(input_coord())
