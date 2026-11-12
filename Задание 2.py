a = str(input('Введите строку: '))
b = list(a)
for i in b[2::3]:
    print(i, end='')