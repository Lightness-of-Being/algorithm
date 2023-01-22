input_set = set([])
test_set = set([])
cnt = 1
for i in range(28):
    input_set.add(input())
for j in range(30):
    test_set.add(str(cnt))
    cnt += 1
res = map(int, test_set - input_set)
res = sorted(res)
print(*res, sep='\n')