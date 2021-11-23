import random
n = int(input('n = '))
a = [[random.randint(-5,15) for j in range(n)] for i in range(n)]
print('a = {0}'.format(a))
for i in range(1, len(a), 2):
    a[i] = sorted(a[i])
print('a = {0}'.format(a))
