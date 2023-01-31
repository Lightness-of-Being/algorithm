from collections import Counter
list_ = []
for i in range(10):
    list_.append(int(input()))
avg = sum(list_)//len(list_)
print(avg)
print(Counter(list_).most_common(1)[0][0])