from collections import deque
N = int(input())
queue = deque(range(1, N + 1))
discard = deque()
while len(queue) > 1:
    discard.append(queue.popleft())
    queue.append(queue.popleft())

discard.append(queue.pop())

print(*discard, end=' ')
