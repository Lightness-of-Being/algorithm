from collections import Counter
res = Counter(input().upper())
res = res.most_common(2)
if len(res) == 1:
    print(res[0][0])
else:
    if res[0][1] == res[1][1]:
        print('?')
    else:
        res = res[0][0]
        print(res)