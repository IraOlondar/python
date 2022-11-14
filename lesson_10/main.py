import datetime
import json
import os.path
from timeit import default_timer
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_msg = f"{datetime.datetime.now():%d.%m.%Y %H:%M:%S} "
        log_msg += f"функция: {func.__name__} "
        log_msg += f"параметры: {', '.join(map(str, args))} "
        res = func(*args, **kwargs)
        log_msg += f"результат: {res}\n"
        with open(func.__name__ + "_log.log", "a", encoding="utf-8") as fp:
            fp.write(log_msg)
        return res
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = default_timer()
        res = func(*args, **kwargs)
        finish = default_timer()
        print(f"Time execution: {round(finish - start, 7)} sec.")
        return res
    return wrapper


def cacher(func):
    @wraps(func)
    def wrapper(args):
        key = str(args)
        cach_file = func.__name__ + "_cach.json"
        
        if not os.path.exists(cach_file):
            cach = {}
        else:
            with open(cach_file, encoding='UTF-8') as file:
                cach = json.load(file)  

        if key not in cach:
            cach[key] = func(args)

            with open(cach_file, "w", encoding="UTF-8") as file:
                json.dump(cach, file, indent=2, ensure_ascii=False)

        return cach[key]
    return wrapper


@logger
@timer
@cacher
def sum_sequence(res):
    a = []
    n = 1 
    summ = 0
    while n <= res:
        summ += (1 + n) ** n
        a.append(summ)
        n += 1
    return summ


def main():
    sum_sequence(3000)
    sum_sequence(9500)
    sum_sequence(1000)
    sum_sequence(2000)
    sum_sequence(9500)
    sum_sequence(6500)


if __name__ == '__main__':
    main()

