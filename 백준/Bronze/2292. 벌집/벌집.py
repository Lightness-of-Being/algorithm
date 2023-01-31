a = [0]
a.append(1)
value = int(input())
index = 1
while True:
    if a[index - 1] < value <=a[index]:
        print(index)
        break
    else:
        a.append(a[index] + 6 * index)
        index += 1