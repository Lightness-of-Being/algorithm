tc = int(input())
input_list = []
for t in range(tc):
    x, y = map(int, input().split())
    input_list.append([x , y])
res = sorted(input_list, key= lambda i:(i[0], i[1]))
for i in res:
    print(*i)