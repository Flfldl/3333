N = int(input())
for i in range(2, N + 1):
    a = 0
    for d in range(1, i // 2 + 1):
        if i % d == 0:
            a += d
    if a == i:
        print(i)

