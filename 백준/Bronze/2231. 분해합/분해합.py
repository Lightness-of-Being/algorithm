input_ = int(input())

for i in range(999999):
    list_ = list(str(i))
    val = i 
    for j in list_:
        val += int(j)
    if input_ == val:
        print(i)
        break
else:
    print(0)
