n, m = list(map(int, input().split()))
c = 0
r = 10 ** 9
ar = [1]

for a in range(0, m):
    if a == 0:
        c = n
        ar.append(n)
    else:
        c = c * n
        ar.append(c)

if sum(ar) > r:
    print("inf")
else:
    print(sum(ar))
