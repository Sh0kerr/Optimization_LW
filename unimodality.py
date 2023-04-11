"""This file relizes the search of unimodality interval ([a, b]) of function f2(x) with a constant step."""

import matplotlib.pyplot as plt
from typing import Union, Tuple
import numpy as np


def func(x: float) -> float:
    """Function that describes f2(x)."""
    return 2 * (x - 1) ** 2 + (0.01 / (1 - 2 * (x ** 2)))


def alg(x: Union[int, float], delta: Union[int, float], a: Union[int, float], b: Union[int, float]) -> Tuple[Union[int, float], Union[int, float], int]:
    """Function that ."""
    k = 0
    x_next= x + delta
    y_next = func(x_next)
    y = func(x)

    while y_next <= y:
        x_next= x + delta
        y_next = func(x_next)
        y = func(x)
        k += 1
    
    a = x
    b = x_next

    return (a, b, k)

a = 0
b = 2
x0, delta = [float(x) for x in input("Print x0 and delta separated by space.\n").split()]

input_set = np.linspace(a, b, 201)
output = [func(x) for x in input_set]

fx0 = func(x0)
fx_left = func(x0 - delta)
fx_right = func(x0 + delta)

if (fx_left >= fx0) and (fx0 >= fx_right):
    print(alg(x0, delta, a, b))
elif (fx_left <= fx0) and (func(x0) <= fx_right):
    delta *= -1
    print(alg(x0, delta, a, b))
elif fx_left >= fx0 <= fx_right:
    a = x0 - delta
    b = x0 + delta
    print(a, b)


plt.plot(input_set, output, label="f2(x)")
plt.legend()
plt.grid()
plt.show()
