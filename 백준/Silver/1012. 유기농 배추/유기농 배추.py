import sys
sys.setrecursionlimit(10000)
T = int(input())

def f(S, i, j):
    if i in range(N) and j in range(M):
        x = (i, j)
        if A[i][j] == 1 and x not in S:
            S.add(x)
            f(S, i, j+1)
            f(S, i, j-1)
            f(S, i-1, j)
            f(S, i+1, j)

for test_case in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    A = [[0 for j in range(M)] for i in range(N)]
    rst = 0
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        A[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                rst += 1
                S = set()
                f(S, i, j)
                for (xi, xj) in S:
                    A[xi][xj] = 0
                # [print(*a) for a in A]
                # print()
    print(rst)