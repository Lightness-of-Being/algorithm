import sys
from collections import deque	
input = sys.stdin.readline
N = int(input())
queue = deque()
flag = 0
cnt = 0
for i in range(N):
    queue.append(int(input()))
for j in deque(reversed(queue)):
    if j > flag:
        flag = j
        cnt += 1
print(cnt)