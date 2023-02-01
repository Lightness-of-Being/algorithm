test_case = int(input())
for t in range(test_case):
    k = int(input())
    n = int(input())
    floor = [x for x in range(1, n + 1)]
    for x in range(k):
        for y in range(1, n):
            floor[y] += floor[y - 1]
    print(floor[-1])