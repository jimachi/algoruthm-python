n = int(input())
mochi = [int(input()) for _ in range(n)]

m = sorted(set(mochi), reverse=True)
c = 0
for i in range(0, len(m)):
    if i == 0:
        c+= 1
    elif m[i - 1] > m[i]:
        c += 1


print(c)

# スマートな方法
# print(len(set(mochi)))
