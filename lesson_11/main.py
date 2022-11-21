from math import sin,cos
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import numpy

def print_graph():
     x = [x for x in numpy.arange(-30, 30, 0.1)]
     y = [(-12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
          x in numpy.arange(-30, 30, 0.1)]
     plt.plot(x, y)
     plt.grid()
     plt.show()


def ff(x):
    return -12 * x ** 4 * sin(cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

def solution(f, interval):
     left, right = interval
     temp = left
     roots = []
     step = 0.1
     while temp < right:
          if f(temp) >= 0 and f(temp + step) <= 0:
               w = fsolve(ff, temp)
               roots.append(*w)
          if f(temp) <= 0 and f(temp + step) >= 0:
               w = fsolve(f, temp)
               roots.append(*w)
          temp += step
     return roots


def top_point(f, interval):
     left, right = interval
     array = []
     temp = left
     while temp < right:
          array.append([f(temp), temp])
          temp += 0.1
     
     data = []
     if array[1][0] > 0:
          data = max(array)
          return {"type": "max", "value": round(data[1], 2)}
     data = min(array)
     return {"type": "min", "value": round(data[1], 2)}


def map_point(f, interval):
     roots = solution(f, interval)
     data = []

     data.append({"type": ("max_border" if f(interval[0]) > 0 else "min_border"), "value": interval[0]})

     for i in range(len(roots) - 1):
          data.append({"type": "root", "value": round(roots[i], 2)})
          data.append(top_point(f, (roots[i], roots[i + 1])))

     data.append({"type": "root", "value": round(roots[i + 1], 2)})
     data.append({"type": ("max_border" if f(interval[1]) > 0 else "min_border"), "value": interval[1]})

     return data


def increasing_funcrion(arr):
     for i in range(len(arr)):
          if (arr[i]["type"] == "root" and
               arr[i - 1]["type"] in ["min", "min_border"] and 
               arr[i + 1]["type"] in ["max", "max_border"]):
               print((arr[i - 1]["value"], arr[i + 1]["value"]))


def decreasing_funcrion(arr):
     for i in range(len(arr)):
          if (arr[i]["type"] == "root" and
               arr[i - 1]["type"] in ["max", "max_border"] and 
               arr[i + 1]["type"] in ["min", "min_border"]):
               print((arr[i - 1]["value"], arr[i + 1]["value"]))


def max_and_min_point(arr):
     for i in range(len(arr)):
          if map_array[i]["type"] in ["max", "min"]:
               print(arr[i]["value"])


def more_null(arr):
     if arr[0]["type"] == "max_border":
          print((arr[0]["value"], arr[1]["value"]))

     for i in range(len(arr)):
          if (arr[i]["type"] == "max" and
               arr[i - 1]["type"] == "root" and 
               arr[i + 1]["type"] == "root"):
               print((arr[i - 1]["value"], arr[i + 1]["value"]))

     if arr[len(arr) - 1]["type"] == "max_border":
          print((arr[len(arr) - 2]["value"], arr[len(arr) - 1]["value"]))


def less_null(arr):
     if arr[0]["type"] == "min_border":
          print((arr[0]["value"], arr[1]["value"]))

     for i in range(len(arr)):
          if (arr[i]["type"] == "min" and
               arr[i - 1]["type"] == "root" and 
               arr[i + 1]["type"] == "root"):
               print((arr[i - 1]["value"], arr[i + 1]["value"]))

     if arr[len(arr) - 1]["type"] == "min_border":
          print((arr[len(arr) - 2]["value"], arr[len(arr) - 1]["value"]))


interval = (-30, 30)
map_array = map_point(ff, interval)


# 1. Определить корни
print(f'\nКорни уравнения для интервала {interval}:')
result = solution(ff, interval)
for i in result:
     print(round(i, 2))

# 2. Найти интервалы, на которых функция возрастает
print(f"\nФункция возрастает на интервалах:")
increasing_funcrion(map_array)

# 3. Найти интервалы, на которых функция убывает
print(f"\nФункция убывает на интервалах:")
decreasing_funcrion(map_array)

# 4. Построить график
print_graph()

# 5. Вычислить вершину
print(f"\nВершины для интервала {interval}:")
max_and_min_point(map_array)

# 6. Определить промежутки, на котором f > 0
print(f"\nf > 0 интервалах:")
more_null(map_array)

# 7. Определить промежутки, на котором f < 0
print(f"\nf < 0 интервалах:")
less_null(map_array)
