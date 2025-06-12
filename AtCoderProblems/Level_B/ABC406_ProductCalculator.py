n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

c = 1
for i in range(0, n):
    x = c * a[i]
    if len(str(x)) > k:
        c = 1
    else:
        c = x

print(c)
