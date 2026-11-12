N, K, R = map(int, input('Введите N, K, R: ').split())
a = 1
while N < R:
    N = N + N * (K / 100)
    a += 1
print(a)