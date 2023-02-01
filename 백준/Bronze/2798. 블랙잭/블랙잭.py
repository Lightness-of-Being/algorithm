from itertools import combinations
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_sum = list(map(sum, list(combinations(input_list, 3))))
input_sum = sorted(input_sum)
res = 0
for i in input_sum:
    if i <= M :
        res = i
print(res)