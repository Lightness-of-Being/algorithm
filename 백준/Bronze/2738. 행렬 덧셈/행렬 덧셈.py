M, N = map(int, input().split())
A = []
B = []
for i in [A, B]:
    for j in range(M):
        i.append(list(map(int, input().split())))
for y in range(M):
    for x in range(N):
        A[y][x] += B[y][x]
    print(*A[y])