A, B = map(int, input().split())
time = int(input())
A = (A +  ((B + time) // 60)) % 24
B = (B + time) % 60
print(A,B)