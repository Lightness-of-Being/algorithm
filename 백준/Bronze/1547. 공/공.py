tc = int(input())
sample = [1, 0 ,0]
for t in range(tc):
    a, b = map(int, input().split())
    sample[a - 1], sample[b - 1] = sample[b - 1], sample[a - 1]
cnt = 1
for i in sample:
    if i == 1:
        print(cnt)
    cnt += 1