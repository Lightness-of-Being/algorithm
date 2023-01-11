A, B = list(map(int, input().split()))
res = A + B
if res == 3:
	if A > B:
		print("A")
	else:
		print("B")

if res == 4:
	if A < B:
		print("A")
	else:
		print("B")

if res == 5:
	if A > B:
		print("A")
	else:
		print("B")