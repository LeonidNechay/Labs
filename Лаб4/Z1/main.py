#Обчислити площу трикутника, якщо трикутник задано довжинами сторін.
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**(1/2)
print('S = {0:.2f}'.format(s))
