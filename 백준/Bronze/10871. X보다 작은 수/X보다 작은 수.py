N, X = map(int, input().split())
input_ = list(map(int, input().split()))
res = []
for num in input_:
    if num < X :
        res.append(num)
res2 = (' '.join(map(str, res)))
print(res2)