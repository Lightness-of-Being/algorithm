list_ = []
for i in range(10):
    list_.append(int(input()) % 42)
res = set(list_)
print(len(res))
