T = int(input())
for t in range(T):
    index = 0
    list_ = list(input())
    dp = [0] * len(list_)
    if list_[0] == 'O':
        dp[0] = 1
    else:
        dp[0] = 0
    for i in list_[1:]:
        index += 1
        if list_[index] == 'O':
            dp[index] = dp[index - 1] + 1
        else:
            dp[index] = 0
    print(sum(dp))