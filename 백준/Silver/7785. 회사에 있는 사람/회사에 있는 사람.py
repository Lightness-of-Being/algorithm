T = int(input())
company = {}
for t in range(T):
    name, being = input().split()
    if being == 'enter':
        company[name]= being
    elif being == 'leave':
        del company[name]
    
res = list(company.keys())
res.sort(reverse=1)
print(*res, sep='\n')