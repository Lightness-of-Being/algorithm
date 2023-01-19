input_ = []	
odd_list = []
for i in range(7):
    input_.append(int(input()))
for j in input_:  
    if int(j)%2 == 1:
        odd_list.append(j)
if odd_list == []:
    print('-1')
else:
    print(sum(odd_list))
    print(min(odd_list))