import random
n = int(input('Введіть кількість чисел: '))
a = []
sum = 1
for i in range(n):
    a.append(random.randint(1, 100))
sum *= a[i]
average_geom = sum ** (1/n)
print('Середне геометричне дорівнює: {0:.2f}'.format(average_geom))
print(a)