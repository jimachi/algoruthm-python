a = list(map(int, input().split()))

for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        c = a[i - 1]
        a[i - 1] = a[i]
        a[i] = c

        if int("".join(map(str, a))) == 12345:
            print("Yes")
            exit()
        else:
            print("No")
            exit()

print("No")
