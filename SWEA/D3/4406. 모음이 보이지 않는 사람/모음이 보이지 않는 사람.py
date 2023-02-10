vowel = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for t in range(T):
    res = []
    input_list = list(input())
    for i in input_list:
        cnt = 0
        for j in vowel:
            if i == j:
                cnt = 1
        if cnt == 0:
            res.append(i)
    print(f'#{t + 1}', end=' ')
    print(*res, sep= '')