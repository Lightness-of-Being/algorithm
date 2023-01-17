point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))
res = []
for i, j, k in zip(point1, point2, point3):
    if i == j:
        res.append(k)
    elif j == k:
        res.append(i)
    else:
        res.append(j)
res = ' '.join(list(map(str, res)))
print(res)