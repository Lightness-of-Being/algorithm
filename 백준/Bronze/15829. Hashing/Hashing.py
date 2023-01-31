N = int(input())
list_ = list(input())
list_num = []
for _ in list_:
    list_num.append(ord(_) - 96)
res = 0
for i, j in zip(list_num, range(len(list_))):
    res += i * (31 ** j)
print(res)
    