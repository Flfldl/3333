max_a = int(input('Введите число очков: '))
while True:
    a1 = int(input('Введите число очков: '))
    if a1 > max_a:
        max_a = a1
    if a1 == -1:
        break
print(max_a)
