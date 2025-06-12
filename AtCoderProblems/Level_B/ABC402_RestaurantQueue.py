from collections import deque

Q = int(input())
queries = [input().split() for _ in range(Q)]
queue = deque()
a = []

for q in queries:
    if q[0] == "1":
        queue.append(q[1])
    elif q[0] == "2":
        a.append(queue[0])

for _ in a:
    print(_)
