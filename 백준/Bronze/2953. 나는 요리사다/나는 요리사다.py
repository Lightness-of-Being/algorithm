other = ['1', '2', '3', '4', '5']
my_dict = {}
res = [0, 0]
score = 0
for t, i in zip(range(5), other):
    score += sum(map(int, input().split()))
    my_dict[i] = score
    if res[1] < score:
        res = [i, score]
    score = 0
print(*res)