people = 0
res = []
for i in range(4):
    unload ,load = map(int, input().split())
    people += load - unload
    res.append(people)
print(max(res))