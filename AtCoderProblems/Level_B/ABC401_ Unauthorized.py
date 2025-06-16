N = int(input())
S = [input() for _ in range(N)]

i = False
c = 0


for s in S:
    if i is False and s == "private":
        c += 1
    if s == "login":
        i = True
    elif s == "logout":
        i = False


print(c)
