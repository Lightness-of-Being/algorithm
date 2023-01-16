T = int(input())
cute_cnt = 0
for i in range(1, T + 1):
    input_ = int(input())
    if input_ == 1:
        cute_cnt += 1
    
if T/2 < cute_cnt:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
