x, r = map(int, input().split())

if r == 1 and x >= 1600 and x <= 2999:
    print("Yes")
elif r == 2 and x >= 1200 and x <= 2399:
    print("Yes")
else:
    print("No")
