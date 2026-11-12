N = int(input())
a = 0
for i in range(N + 1):
    for b in range(i, N + 1):
        a += i + b
print(a)
