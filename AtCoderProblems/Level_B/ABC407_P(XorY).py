x = list(map(int, input().split()))

c = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i + j >= x[0] or i - j >= x[1] or j - i >= x[1]:
            c += 1


print(c / 36)
