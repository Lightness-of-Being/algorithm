from collections import deque
N, K = map(int, input().split())
q = deque(x for x in range(1, N + 1))
res = []
for i in range(1, N + 1):
    q.rotate(-K + 1)
    res.append(q.popleft())
print(f'<{", ".join(map(str, res))}>')