A, B, C = list(map(int, input().split()))
if A == B and B == C:
    res = 10000 + A * 1000
    print(res)
elif A != B and B != C and C != A:
    res = max(A, B, C) * 100
    print(res)
else:
    list_ = [A, B, C]
    sample = list(set(list_))
    list_add = 0
    sample_add = 0
    for i in list_:
        list_add += i
    for j in sample:
        sample_add += j
    val = list_add - sample_add
    res = 1000 + val * 100
    print(res)