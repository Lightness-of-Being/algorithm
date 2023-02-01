from math import factorial as fac
a, b = map(int, input().split())
res = fac(a)//(fac(b) * fac(a - b))
print(res)