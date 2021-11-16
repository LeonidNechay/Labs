#Впорядкувати елементи масиву за спаданням.
import random
n = int(input('Кількість елементів в списку: '))
a = []
b = []
for i in range(n):
    a.append(random.randint(1, 100))
b=sorted(a, reverse=True)
print(a)
print(b)