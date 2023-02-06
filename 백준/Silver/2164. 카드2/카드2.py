from collections import deque
N = int(input())
q = deque(x for x in range(1, N + 1))
while True:
    if len(q) == 1:
        print(*q)
        break
    else:
        q.popleft()
        q.rotate(-1)