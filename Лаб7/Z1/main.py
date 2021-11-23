'''
Визначити суму додатних елементів матриці з першим парним і другим непарним індексами.
'''
n = int(input('n='))
m = int(input('m='))
a = [[float(input('a[{0}][{1}]: '.format(i, j))) for j in range(m)] for i in range(n)]
s = 0
for i in range(0, len(a), 2):
    for j in range(1, len(a[i]), 2):
        if a[i][j] > 0:
             s += a[i][j]
print(s)