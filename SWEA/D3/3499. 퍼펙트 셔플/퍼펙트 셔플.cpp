from math import *
T = int(input())
for t in range(T):
    num = int(input())
    res = []
    input_list = list(input().split())
    list_helf = input_list[:ceil(num/2)]
    list_another = input_list[ceil(num/2):]
    if num % 2 == 0:
        for i in range(len(list_helf)):
            res.append(list_helf[i])
            res.append(list_another[i])
    else:
        for i in range(len(list_another)):
            res.append(list_helf[i])
            res.append(list_another[i])
        res.append(list_helf[-1])
    print(f'#{t + 1}', end= ' ')
    print(*res)