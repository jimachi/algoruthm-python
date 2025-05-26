n, a, b = map(int, input().split())
z = 0
for c in range(1, n + 1):
    x = sum(map(int, str(c)))
    if a <= x <= b:
        z += c


print(z)
