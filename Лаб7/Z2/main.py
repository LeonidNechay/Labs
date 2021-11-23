import random
def random_matrix(n, m):
    '''
    :param n: Кількість рядків
    :param m: Кількість стовпців
    :return: Генеруємо матрицю
    '''
    return [[random.randint(0, 5) for j in range(m)] for i in range(n)]
n = int(input('n = '))
m = int(input('m = '))
a = random_matrix(n, m)
b = random_matrix(n, m)
print('a = {0}'.format(a))
print('b = {0}'.format(b))
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 0:
            a[i][j] = b[i][j]
print('a = {0}'.format(a))
