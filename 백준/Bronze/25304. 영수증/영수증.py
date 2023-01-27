total = int(input())
T = int(input())
list_ = []
for t in range(T):
    A, B = map(int, input().split())
    price = A * B
    list_.append(price)
if total == sum(list_):
    print('Yes')
else:
    print('No')