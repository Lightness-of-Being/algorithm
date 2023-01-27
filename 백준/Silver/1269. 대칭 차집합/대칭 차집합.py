trash = input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))

X = A - B
Y = B - A
print(len(X) + len(Y))