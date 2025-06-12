n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

c = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if j in a:
            continue
        else:
            print(c)
            exit()
    c += 1
    a.pop()

print(c)
