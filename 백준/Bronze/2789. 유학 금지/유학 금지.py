censor = 'CAMBRIDGE'
input_ = input()
res = []
for i in input_[:]:
    res.append(i)
    for j in censor[:]:
        if i == j :
            res.remove(j)
print(*res, sep='')
            
        