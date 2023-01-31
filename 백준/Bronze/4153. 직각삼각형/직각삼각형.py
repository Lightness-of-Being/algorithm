while True:
    input_list = sorted(list(map(int, input().split())))
    square = []
    if input_list == [0, 0, 0]:
        break
    else:
        for i in input_list:
            square.append(i**2)
        if square[0] + square[1] == square[2]:
            print('right')
        else:
            print('wrong')