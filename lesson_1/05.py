#Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

def input_coord(a):
    name = ["X", "Y"]
    arr = []
    print(f"Введите координаты точки {a}")
    for nam in name:
        not_error = False
        while  not not_error:
            try:
                number = int(input(f"{nam} = "))
                not_error = True
                arr.append(number)          
            except ValueError:
                print("Введено не число!")
    return arr

def length_segment(a, b):
    print(f"Длина отрезка: {round((((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5), 2)}")


point_a = input_coord("A")
point_b = input_coord("B")

length_segment(point_a, point_b)
