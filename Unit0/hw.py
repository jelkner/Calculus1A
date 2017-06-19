import math


def cube_root(x):
    return x ** (1/3) if x >= 0 else -((-x) ** (1/3))


def f(x):
    return (x - cube_root(x) + math.cos(x)) / ((x ** 2) - 4)
