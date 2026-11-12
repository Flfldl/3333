x = int(input())
a = 0
c = int(x ** 0.5) + 1
for i in range(1, c):
    for b in range(i, c):
        if i ** 2 + b ** 2 == x:
            a += 1
print(a)
