import math


def f(x):
    return math.sqrt(3 - 5 * x + x ** 2 + x ** 3) / (x - 1)


def g(x):
    return x / math.tan(2 * x)


def h(x):
    return (abs(x) + math.sin(x)) / x ** 2


def j(x):
    return math.sin(13 / x)
