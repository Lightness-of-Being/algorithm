from collections import deque
H = deque([x for x in range(24)])
M = deque([x for x in range(60)])
A, B = map(int, input().split())
if B - 45 < 0 :
    A -= 1
print(H[A],M[B-45])