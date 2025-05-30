import math 

x = list(map(int, input().split()))

x.sort()

if math.prod(x[:2]) == x[-1]:
    print("Yes")
else:
    print("No")
