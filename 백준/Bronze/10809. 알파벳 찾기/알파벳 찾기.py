alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

input_ = input()
res = [-1 for x in range(len(alphabet_list))]
cnt = 0
for i in alphabet_list:
    for j in input_:
        if i == j:
            res[cnt] = (input_.index(i))
    cnt += 1
    
print(*res)