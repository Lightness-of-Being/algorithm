T = int(input())
for t in range(1, T +1):
    input_ = input().split()
    res = []
    for i in input_:
        res.append(i[::-1])
    print(*res)