n = int(input())
a = list(map(int, input().split()))

c = 0
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        c += 1
        if c == 2:
            print("Yes")
            exit()
    else:
        c = 0

print("No")
