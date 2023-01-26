T = int(input())
res_list = []
for t in range(T):
    input_ = int(input())
    if input_ == 0:
        res_list.pop()
    else:
        res_list.append(input_)
print(sum(res_list))