x, y, w, h = map(int, input().split())
list_ = [x, y, w - x, h - y]
print(min(list_))