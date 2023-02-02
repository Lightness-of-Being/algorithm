from collections import deque
tc = int(input())
res = [0]
input_list = list(map(int, input().split()))
input_q = deque(input_list)
high = []
low = []
res = 0
index = 0
flag = input_q.popleft()

for i in input_q:
    if input_list[index] < input_q[index]:
        if res < input_q[index] - flag:
            res = input_q[index] - flag
    else:
        flag = input_q[index]
    index += 1
print(res)