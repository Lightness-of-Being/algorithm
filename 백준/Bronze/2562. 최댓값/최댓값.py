list_ = []
for i in range(9):
    input_ = int(input())
    list_.append(input_)
res = max(list_)
res_index = list_.index(res)
print(res)
print(res_index + 1)