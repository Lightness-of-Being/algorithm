from collections import deque
T = int(input())
for t in range(T):
    list_ = deque(map(int, input().split()))
    list_.popleft()
    avg = sum(list_)/len(list_) 
    cnt = 0
    for i in list_:
        if i > avg:
            cnt += 1
    res = cnt/len(list_)*100
    print(f'{res:.3f}%')