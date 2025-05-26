n = int(input())
a = list(map(int, input().split()))

alice, bob = 0, 0

c = 0
while len(a) != 0:
    mx = max(a)
    max_index = a.index(mx)
    if c % 2 == 0:
        alice += mx
    else:
        bob += mx
    c += 1
    del a[max_index]

print(alice - bob)


# スマートな方法
# n = int(input())
# a = list(map(int, input().split()))

# a.sort(reverse=True)

# alice = sum(a[::2])
# bob = sum(a[1::2])

# print(alice - bob)
