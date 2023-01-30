import sys
input = sys.stdin.readline
A, B = input().split()
A = map(int, A)
B = map(int, B)
print(sum(A) * sum(B))