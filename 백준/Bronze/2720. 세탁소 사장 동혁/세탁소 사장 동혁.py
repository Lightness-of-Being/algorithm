T = int(input())
coin = [25, 10, 5, 1]
for t in range(T):
    res_list = []
    change = int(input())

    for m in coin:
        Q,R = divmod(change, m)
        res_list.append(Q)
        change -= m * Q
    print(*res_list)