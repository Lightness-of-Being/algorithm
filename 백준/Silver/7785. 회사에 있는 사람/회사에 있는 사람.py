import sys
T = int(sys.stdin.readline())
company = {}
for t in range(T):
    name, being = sys.stdin.readline().split()
    if being == 'enter':
        company[name]= being
    elif being == 'leave':
        del company[name]
    
res = list(company.keys())
res.sort(reverse=1)
print(*res, sep='\n')