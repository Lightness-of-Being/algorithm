input_ = input()
zero_index = input_.index('0')
cnt1 = 0
cnt2 = 0
for i in input_[:zero_index]:
    if i == '@':
        cnt1 += 1
for j in input_[zero_index:]:
    if j == '@':
        cnt2 += 1
print(cnt1,cnt2)