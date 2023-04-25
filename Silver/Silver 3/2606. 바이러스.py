from collections import deque

n = int(input())
m = int(input())

graph = [[False] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def bfs(v):
    dq = deque([v])

    while dq:
        v = dq.popleft()
        
        for i in range(n+1):
            if not visited[i] and graph[v][i]:
                dq.append(i)
                visited[i] = True

bfs(1)
# 1은 제외
print(sum(visited) - 1)