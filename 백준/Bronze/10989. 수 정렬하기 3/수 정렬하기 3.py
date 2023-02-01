import sys
input = sys.stdin.readline
T = int(input())
num = [0] * 10001
for _ in range(T):
    cnt = int(input())
    num[cnt] += 1
for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
