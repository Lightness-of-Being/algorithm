from itertools import combinations as combi
a, b = map(int, input().split())
print(len(list(combi(range(a), b))))