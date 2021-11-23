import random
n = int(input('n = '))
m = int(input('m = '))
num = m
a = [[random.randint(-5, 5) for j in range(m)] for i in range(n)]
print(*a, sep='\n')
for j in range(m):
    for i in range(n):
        if a[i][j] == 0:
            num -= 1
            break
print(num)