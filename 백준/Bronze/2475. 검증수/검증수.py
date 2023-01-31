input_list = list(map(int, input().split()))
res = 0
for i in input_list:
    res += i**2
res %= 10
print(res)