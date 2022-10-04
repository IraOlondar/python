# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.

import math

def roots_quad_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D == 0:
        x = round(-b / 2 / a, 2)
        return f"x = {x}"
    elif D > 0:
        x1 = round((-b + D ** (1 / 2)) / (2 * a), 2)
        x2 = round((-b - D ** (1 / 2)) / (2 * a), 2)
        return f"x1 = {x1}; x2 = {x2}"
    return "Корней нет"

def roots_quad_equation_lib(a, b, c):
    D = b ** 2 - 4 * a * c 
    if D == 0:
        x = round(-b / 2 / a, 2)
        return f"x = {x}"
    elif D > 0:
        x1 = round((-b + math.sqrt(D)) / (2 * a), 2) 
        x2 = round((-b - math.sqrt(D)) / (2 * a), 2)
        return f"x1 = {x1}; x2 = {x2}"
    else:
        return "Корней нет"

A = 4
B = 6
C = -55

#4x² + 6x - 55 = 0

print(roots_quad_equation(A, B, C))
print(roots_quad_equation_lib(A, B, C))

