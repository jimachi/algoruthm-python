n = int(input())
s = str(input())
t = str(input())


c = 0
for a, b in zip(s, t):
    if a != b:
        c += 1

print(c)
