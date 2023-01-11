input_ = int(input())
res = [

]
while input_ > -1:
	res.append(input_)
	input_ -= 1
t = ''
res.sort()
for i in res:
	t = 2 ** i
	print(t, end=' ')	