import math


def g(x: int):
    if x == 0:
        return 9
    elif x == 1:
        return 35
    elif x > 1:
        return math.sin(g(x - 1) + math.cos(g(x-2)))


s = g(7) + g(9)
print('s = {0}'.format(s))