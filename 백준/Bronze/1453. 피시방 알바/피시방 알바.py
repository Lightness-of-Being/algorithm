import sys
input = sys.stdin.readline
table = [0]*100
res = 0
T = int(input())
list_ = list(map(int, input().split()))
for i in list_:
    if table[i - 1] == 0:
        table[i - 1] = 1
    else:
        res += 1
print(res)