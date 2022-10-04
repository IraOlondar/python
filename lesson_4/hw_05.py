# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(f, st):
    with open(f, "w") as data:
        data.write(st)

def rand():
    return random.randint(0,101)

def create_list(k):
    lst = [rand() for i in range(k + 1)]
    return lst  

def create_str(ar):
    lst = ar[::-1]
    text = ""
    if len(lst) < 1:
        text = "x = 0"
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                text += f"{lst[i]}x^{len(lst) - i - 1}"
                if lst[i+1] != 0:
                    text += " + "
            elif i == len(lst) - 2 and lst[i] != 0:
                text += f"{lst[i]}x"
                if lst[i+1] != 0:
                    text += " + "
            elif i == len(lst) - 1 and lst[i] != 0:
                text += f"{lst[i]} = 0"
            elif i == len(lst) - 1 and lst[i] == 0:
                text += " = 0"
    return text

def sq_ur(k):
    if "x^" in k:
        i = k.find("^")
        num = int(k[i+1:])
    elif ("x" in k) and ("^" not in k):
        num = 1
    else:
        num = -1
    return num

def k_ur(k):
    if "x" in k:
        i = k.find("x")
        num = int(k[:i])
    return num

def calc_ur(st):
    st = st[0].replace(" ", "").split("=")
    st = st[0].split("+")
    lst = []
    l = len(st)
    k = 0
    if sq_ur(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    ii = l - 1
    while ii >= 0:
        if sq_ur(st[ii]) != -1 and sq_ur(st[ii]) == i:
            lst.append(k_ur(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst

k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))

f1 = "file_hw_5_1.txt"
f2 = "file_hw_5_2.txt"
f_res = "file_hw_5_res.txt"

write_file(f1, create_str(create_list(k1)))
write_file(f2, create_str(create_list(k2)))

with open(f1, "r") as data:
    st1 = data.readlines()
with open(f2, "r") as data:
    st2 = data.readlines()

lst1 = calc_ur(st1)
lst2 = calc_ur(st2)
l_min = min(len(lst1), len(lst2))
lst_new = [lst1[i] + lst2[i] for i in range(l_min)]

if len(lst1) > len(lst2):
    for i in range(l_min, len(lst1)):
        lst_new.append(lst1[i])
else:
    for i in range(l_min, len(lst2)):
        lst_new.append(lst2[i])

write_file(f_res, create_str(lst_new))
with open(f_res, "r") as data:
    st3 = data.readlines()
    
print(f"Первый многочлен: {st1[0]}")
print(f"Второй многочлен: {st2[0]}")
print(f"Итоговый многочлен: {st3[0]}")
