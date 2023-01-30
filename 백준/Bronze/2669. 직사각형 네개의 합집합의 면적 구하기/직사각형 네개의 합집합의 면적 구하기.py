coordinate = [[0]*101 for _ in range(101)]
for k in range(4):
    a_x, a_y, b_x, b_y = map(int, input().split())
    for i in range(a_x, b_x):
        for j in range(a_y, b_y):
            coordinate[i][j] = 1
res = sum(list(map(sum, coordinate)))
print(res)