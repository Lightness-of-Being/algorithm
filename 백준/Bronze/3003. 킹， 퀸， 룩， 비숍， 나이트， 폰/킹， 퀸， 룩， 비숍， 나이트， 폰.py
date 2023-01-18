king = 1
queen = 1
rooks = 2
bishops = 2
knights = 2
pawns = 8
sample = [king, queen, rooks, bishops, knights, pawns]
input_ = list(map(int, input().split()))
res = []
for i ,j in zip(input_, sample):
    res.append(j - i)
print(*res)