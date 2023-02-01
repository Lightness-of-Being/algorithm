from math import factorial as fac
a = int(input())
cnt = 0
list_ = list(reversed(list(str(fac(a)))))
index = 0
for i in list_:
    index += 1
    if i != '0':
        print(index - 1)
        break