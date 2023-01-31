while True:
    input_ = input()
    if input_ == '0':
        break
    else:
        input_reverse = input_[::-1]
        if input_ == input_reverse:
            print('yes')
        else:
            print('no')