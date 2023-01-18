input_ = list(map(int, input().split()))
input_init = input_
cnt = 0
while True:
    if input_ == [1, 2, 3, 4, 5]:
        break
    
    else:
        if input_[0] > input_[1]:
            input_[0], input_[1] = input_[1], input_[0]
            cnt += 1
            print(*input_)
        if input_[1] > input_[2]:
            input_[1], input_[2] = input_[2], input_[1]
            cnt += 1
            print(*input_)
        if input_[2] > input_[3]:
            input_[2], input_[3] = input_[3], input_[2]
            cnt += 1
            print(*input_)
        if input_[3] > input_[4]:
            input_[3], input_[4] = input_[4], input_[3]
            cnt += 1
            print(*input_)