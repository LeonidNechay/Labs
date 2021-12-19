num = []
file = open('text1.txt')
for el in file:
    n = float(el)
    if n < 0:
        num.append(n)
print(max(num))
file.close()
