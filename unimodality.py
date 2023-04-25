"""Релизация поиска интервала унимодальности ([a, b]) функции f2(x) с постоянным шагом."""

import matplotlib.pyplot as plt
from typing import Union, Tuple
import numpy as np
import pandas as pd


def func(x: float) -> float:
    """Задание функции f2(x)"""
    return 2 * (x - 1) ** 2 + (0.01 / (1 - 2 * (x ** 2)))


def step(delta: float) -> float:
    """Функция шага"""
    return delta


a = 0
b = 2
x0 = 0
k_limit = 500
# x0, delta = [float(x) for x in input("Print x0 and delta separated by space.\n").split()]

# input_set = np.linspace(a, b, 201)
# output = [func(x) for x in input_set]
delta_range = np.linspace(0.001, 0.025, 25)

b_list = []
ba_list = []
k_list = []



for delta in delta_range:
    a = []
    fx0 = func(x0)
    fx_left = func(x0 - delta)
    fx_right = func(x0 + delta)

    if fx_left >= fx0 >= fx_right:
        delta = delta
    elif fx_left <= fx0 <= fx_right:
        delta *= -1
    elif fx_left >= fx0 <= fx_right:
        exit(0)

    k = 0

    x_next = x0
    while True:
        x_prev = x_next
        x_next += step(delta)
        if func(x_next) > func(x_prev):
            a = x_prev
            b = x_next
            break
        else:
            k += 1

    b_list.append(b)
    ba_list.append(b-a)
    k_list.append(k)


df = pd.DataFrame()
df["delta"] = delta_range
df["x0"] = [2 for _ in range(25)]
df["b"] = b_list
df["b - a"] = ba_list
df["k"] = k_list

print(df)

"""Вывод графика функции""" 
# plt.plot(input_set, output, label="f2(x)")
# plt.legend()
# plt.grid()
# plt.show()
