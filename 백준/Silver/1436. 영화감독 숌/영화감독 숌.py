list_ = []
input_ = int(input())
cnt = 0
num = 0
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == input_:
        print(num)
        break
    num += 1