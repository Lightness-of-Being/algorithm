T = int(input())
for t in range(T):
    list_input = list(map(int, input().split()))
    max_score = max(list_input)
    min_score = min(list_input)
    list_input.remove(max_score)
    list_input.remove(min_score)
    if 4 <= (max(list_input) - min(list_input)):
        print('KIN')
    else:
        print(sum(list_input))