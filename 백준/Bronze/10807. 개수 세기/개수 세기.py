import sys
def input():
    return sys.stdin.readline()
T = int(input())
input_list = list(map(int, input().split()))
input_key = int(input())
cnt = 0
for i in input_list:
    if i == input_key:
        cnt += 1
print(cnt)