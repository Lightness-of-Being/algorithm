A = int(input())
B = int(input())
C = int(input())
value = A * B * C
for i in range(10):
    print(str(value).count(str(i)))