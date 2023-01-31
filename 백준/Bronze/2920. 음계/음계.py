asc = [x for x in range(1, 9)]
des = [x for x in range(8, 0, -1)]
input_list = list(map(int, input().split()))
if input_list == asc:
    print('ascending')
elif input_list == des:
    print('descending')
else:
    print('mixed')