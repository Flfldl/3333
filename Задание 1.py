b = 0
for a in range(100, 1000):
    if a % 17 == 0:
        print(a, end=' ')
        b += 1
print()
print(b)