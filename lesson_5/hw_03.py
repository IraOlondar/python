# Реализуйте RLE алгоритм: 
# реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

file_str = "str.txt"
file_zip = "zip.txt"

with open(file_str, "w") as data:
    data.write('WWWWWDDDWWWWWWWBWWWWWWWWGGGGGGGGGWWWWBBBWWWWWWWWWWWWTTTTTTTTTWWWWWWWWWWWWBBWWWWWWWWWWWWWW')

with open(file_str, "r") as file:
    str_in = file.read()

def rle_zip(strin):
    str_zip = ""
    count = 1
    char = strin[0]
    for i in range(1, len(strin)):
        if strin[i] == char:
            count += 1
        else:
            str_zip = str_zip + str(count) + char
            char = strin[i]
            count = 1
    str_zip = str_zip + str(count) + char
    return str_zip


def rle_unzip(str_zip):
    str_unzip = ""
    elem_count = ""
    for i in range(len(str_zip)):
        if str_zip[i].isdigit():
            elem_count += str_zip[i]
        else:
            str_unzip += str_zip[i] * int(elem_count)
            elem_count = ""
    return str_unzip

with open(file_zip, "w") as file:
    string_zip = rle_zip(str_in)
    file.write(string_zip)

print(f"Строка: '{str_in}'")
print(f"Архив: '{rle_zip(str_in)}'")
print(f"Степень сжатия: {round(len(str_in) / len(string_zip), 1)}")

print(f"Разархивированная строка: '{rle_unzip(string_zip)}'")