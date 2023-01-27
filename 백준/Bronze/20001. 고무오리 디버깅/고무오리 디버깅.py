cnt = 0
start = input()
if start == '고무오리 디버깅 시작':
	while True:
		input_ = input()
		if input_ == '문제':
			cnt += 1
		elif input_ == '고무오리':
			if cnt > 0:
				cnt -= 1
			else:
				cnt += 2
		elif input_ == '고무오리 디버깅 끝':
			break
	if cnt <= 0:
		print('고무오리야 사랑해')
	else:
		print('힝구')