T = int(input())
list_ = list(map(int, input().split()))
max_num = max(list_)
list_new = []
for i in list_:
    list_new.append(i/max_num * 100)
print(sum(list_new)/len(list_new))
