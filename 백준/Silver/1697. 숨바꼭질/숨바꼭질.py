from collections import deque

N, K = map(int, input().split())
limit = 100001
visited = [0] * limit
def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()       # queue 왼쪽에서 꺼낸다 선입선출
        if x == K:
            print(visited[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i < limit and not visited[i]:    # 범위를 만족하고 아직 방문 안했다면
                visited[i] = visited[x] + 1           # 현재 숫자(시간)에 1초 추가
                queue.append(i)                       # 큐에 추가 
BFS()