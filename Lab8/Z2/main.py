import math


def f(x):
    return math.sqrt(4 * x + math.sin(math.sqrt(x ** 3)))


def i(a,b):
    return f(a) * (b-a)


x = float(input('x = '))
a = float(input('a = '))
b = float(input('b = '))
s = i(a, 3) + i(a, b)
print('s = {0:.2f}'.format(s))