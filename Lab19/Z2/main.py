numbers = []
with open('text2.txt') as file:
    for el in file:
        n = float(el)
        numbers.append(n)
max_num = max(numbers)
for el in numbers:
    if el == 0:
        el = max(numbers)
with open('task2.txt', 'w') as file2:
    for el in numbers:
        file2.write(str(el) + '\n')

