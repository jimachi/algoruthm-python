n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

t_prev, x_prev, y_prev = 0, 0, 0

for t, x, y in schedule:
    dt = t - t_prev
    dist = abs(x - x_prev) + abs(y - y_prev)

    if dist > dt or (dt - dist) % 2 != 0:
        print("No")
        exit()

    t_prev, x_prev, y_prev = t, x, y

print("Yes")
