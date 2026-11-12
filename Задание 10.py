C = float(input('Введите температуру: '))
a = 0
while C != 0:
    C1 = float(input('Введите температуру: '))
    if C1 < C:
        a += 1
    if C == 0:
        break
    C = C1

    print(a - 1)
