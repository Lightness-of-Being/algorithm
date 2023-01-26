
from collections import Counter

test_cace = int(input())
for t in range(test_cace):
    test_num = int(input())
    input_list = list(map(int, input().split()))
    input_dict = Counter(input_list)
    max_value = max(input_dict.values())
    res_list = []
    for key, value in input_dict.items():
        if value == max_value:
            res_list.append(key)
    print(f'#{t+1} {max(res_list)}')