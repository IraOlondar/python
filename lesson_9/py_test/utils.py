def check_quarter(x, y):
    quarter = 4
    if x > 0 and y > 0:
        quarter = 1
    elif x < 0 and y > 0:
        quarter = 2
    elif x < 0 and y < 0:
        quarter = 3
    
    return quarter


def summ(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    return s


def mult_list(lst):
    l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
    return new_lst


def fractional_part_difference(lst):
    arr = [round(i % 1, 2) for i in lst if i % 1 != 0]
    return max(arr) - min(arr)