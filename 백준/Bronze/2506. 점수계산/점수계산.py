N = int(input())
input_ = list(map(int, input().split()))
res = [0 for i in range(N + 1)]
index = -1
cnt = 0
input_.append(0)
for i in (input_):
    index += 1
    if index == 0:
         if input_[index] == 1:
              res[index] = 0
              cnt = 1
         else:
              res[index] = 0
              cnt = 0
             
    else :
         if input_[index] == 1:               # 본인이 1이고 전에것이 0이면
              if input_[index - 1] == 0:
                   res[index] = 0
                   cnt = 1
              else :
                   res[index] = 0
                   cnt += 1
         elif input_[index] == 0:
              if input_[index - 1] == 1:
                   res[index] = cnt
                   cnt = 0
result = 0
cnt2 = 0
for i in res:
     for j in range(i + 1):
          cnt2 += j
print(cnt2)