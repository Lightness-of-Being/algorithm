cnt = 0
num = input()
init = num
if int(init) < 10:
    init = '0' + init

while True:
    cnt += 1
    if int(num) < 10:
        num = '0' + num 
    num_add = str(int(num[-2]) + int(num[-1]))
    num = num[-1] + num_add[-1]
    if init == num:
        print(cnt)
        break
