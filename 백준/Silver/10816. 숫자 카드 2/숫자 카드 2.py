from collections import Counter

M = int(input())
M_list = list(map(int, input().split()))
N = int(input())
N_list = list(map(int, input().split()))
res = []
dict = Counter(M_list)
for i in N_list:
    print(dict[i], end=' ')