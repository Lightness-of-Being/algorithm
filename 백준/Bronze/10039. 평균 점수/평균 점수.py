A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
list_ = [A, B ,C ,D ,E]  
cnt = 0
for i in list_:      
    if i < 40:
        list_[cnt] = 40
    cnt += 1
print(int(sum(list_)/5))