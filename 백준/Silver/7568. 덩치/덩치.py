from collections import deque 
tc = int(input())
input_list = []
res = []
cnt = 0
for t in range(tc):
    input_list.append(list(map(int, input().split())))
for i in input_list:
    rank = 1
    for j in input_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    res.append(rank)
print(*res)