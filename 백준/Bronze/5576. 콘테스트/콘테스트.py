w_score = 0
k_score = 0
w_list = []
k_list = []
for i in range(10):
    w_list.append(int(input()))
for i in range(10):
    k_list.append(int(input()))
w_list = sorted(w_list, reverse=1)
k_list = sorted(k_list, reverse=1)
for i in range(3):
    w_score += w_list[i]
    k_score += k_list[i]
print(w_score, k_score)