a = int(input('Введите число: '))
while a**0.5 != int(a**0.5):
    print('Не подходит')
    a = int(input())
else:
    print('Всё четко')