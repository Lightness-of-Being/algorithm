T = int(input())
input_set = set()
for t in range(T):
    input_set.add(input())
res = sorted(list(input_set))
res = sorted(res, key= len)
print(*res, sep='\n')
