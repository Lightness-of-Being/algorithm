T = int(input())
list_ = []
for t in range(T):
    input_ = int(input())
    list_.append(input_)
list_.sort()
for j in list_:
    print(j)