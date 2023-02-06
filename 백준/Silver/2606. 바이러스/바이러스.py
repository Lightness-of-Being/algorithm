com_num = int(input())
T = int(input())
res = []
graph = [[] for _ in range(com_num + 1)]
for i in range(T):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited =[False] * (com_num + 1)

def DFS(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  res.append(v)
  for i in graph[v]:
    if not visited[i]:
      DFS(graph, i, visited)


DFS(graph, 1, visited)
print(len(res) - 1)