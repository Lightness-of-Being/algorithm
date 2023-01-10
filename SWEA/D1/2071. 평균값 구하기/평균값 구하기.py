T = int(input())
for t in range(1, T + 1):
	a1,a2,a3,a4,a5,a6,a7,a8,a9,a10 = list(map(int,input().split()))
	res = (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10) / 10
	res = round(res)
	print(f'#{t} {res}')