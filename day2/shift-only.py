n = int(input())
a = list(map(int, input().split()))

counts = []

for m in a:
    c = 0
    while m % 2 == 0:
        m = m // 2
        c += 1
    counts.append(c)


print(min(counts))
