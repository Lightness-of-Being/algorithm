
T = int(input())
for t in range(1, T + 1):
	list_ = list(map(int,input().split()))
	res = max(list_)
	print(f'#{t} {res}')