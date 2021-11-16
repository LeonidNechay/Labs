a = []
num = float(input('Введіть число: '))
n = int(input('Введіть кількість вимірів: '))
for i in range(n):
    x = float(input('Введіть {0} координату: '.format(i+1)))
    a.append(x*num)
print('Добуток вектора а на число {0} = {1}'.format(num, a))