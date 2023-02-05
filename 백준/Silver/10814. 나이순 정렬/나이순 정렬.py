tc = int(input())
input_list = []
for t in range(tc):
    year, name = input().split()
    input_list.append([int(year) , name])
res = sorted(input_list, key= lambda x:x[0])
for i in res:
    print(*i)