T = int(input())
for t in range(T):
    num, char = input().split()
    num = int(num)
    res = []
    for i in char:
        res.append(i * num)
    print(*res, sep='')