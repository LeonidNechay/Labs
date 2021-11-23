import random


def random_matrix(n, m):
    '''
    :param n: Кількість рядків
    :param m: Кількість стовпців
    :return: Генеруємо матрицю
    '''
    return [[random.randint(0, 10) for j in range(m)] for i in range(n)]


def input_vector(n,vector_title):
    ''':param n: Кількість елементів у векторі
    :param vector_title: Назва вектора
    :return: Введення вектора
    '''
    return [float(input('{0}[{1}] = '.format(vector_title, i))) for i in range(n)]


eps=0.0001
n = int(input('n = '))
m = int(input('m = '))
a = random_matrix(n, m)
print(*a, sep='\n')
x = input_vector(m, 'x')
b = input_vector(n, 'b')
is_x_solution = True
for i in range(len(a)):
    s=0
    for j in range(len(a[i])):
        s += a[i][j]*x[j]
    if abs(s-b[i])>eps:
        is_x_solution = False
        break
if is_x_solution:
    print('Ax = B ')
else:
    print('Ax != B')