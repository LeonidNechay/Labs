#Знайти добуток елементів масиву В з непарними номерами.
n = int(input('Введіть кількість елементів масива: '))
b = []
result = 1
variable_1 = 0
variable_2 = 1
i_1 = i_2 = 1
for i in range(1, n+1):
    if i % 2 == 0:
        while i_1 <= i:
            variable_1 += 1/i_1
            i_1 += 1
        b.insert(i, variable_1)
    else:
        while i_2 <= i:
            variable_2 *= i_2
            sum = (variable_2 / 2) + 3
            i_2 += 1
        b.insert(i, sum)
for i in range(1, n+1):
    if not i % 2 == 0:
        result *= b[i-1]
print(b)
print(result)
