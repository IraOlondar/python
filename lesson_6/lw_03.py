# Дана строка: 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул' 
# Необходимо получить словарь, в котором ключи – слова, значения – количество слов в строке: 
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}


from functools import reduce
from pprint import pprint


file_str = "lesson_6/jack.txt"

with open(file_str, "r", encoding="UTF-8") as file:
    string = file.read()

replace_values = [("\n", " "), (",", ""), (".", "")]
[string := string.replace(a, b) for a, b in replace_values]

string = string.lower()

arr = string.split()

res_arr = {}

for i in arr:
    res_arr[i] = res_arr.get(i, 0) + 1

print(arr)
print("\n")
pprint(res_arr)