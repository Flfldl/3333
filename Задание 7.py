N = int(input('Введите свой ответ: '))
a = 1
while a < N:
    a = a * 2
if a == N:
    print('верно')
elif a != N:
    print('неверно')
