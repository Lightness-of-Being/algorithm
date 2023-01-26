T = int(input())
for t in range(T):
    input_ = input()
    while True:
        input_2 = input_.replace('()','')
        if input_ == input_2:
            break
        input_ = input_2
    if input_2 == '':
        print('YES')
    else:
        print('NO')
            