up, down, gool = map(int, input().split())
res = (gool - down) / (up - down)
print(int(res) if res == int(res) else int(res) + 1)