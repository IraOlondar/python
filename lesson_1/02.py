# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def input_data():
    name = ["X", "Y", "Z"]
    a = []
    for i in name:
        a.append(input(f"Введите значение {i}: "))
    return a


def check_condition(list):
    return not (list[0] or list[1] or list[2]) == (not list[0] and not list[1] and not list[2])


if check_condition(input_data()) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")