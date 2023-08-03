from collections import deque

n, m, v = map(int, input().split())

# 간선 정보
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# DFS
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True

    print(v, end=" ")

    # i를 방문하지 않았고 v와 연결되어 있다면
    for i in range(1, n+1):
        if not visited[i] and graph[v][i]:
            dfs(graph, i, visited)

# BFS
def bfs(graph, v, visited):
    dq = deque([v])

    # 현재 노드 방문 처리
    visited[v] = True

    # 큐가 빌때까지 반복
    while dq:
        # 큐에서 원소 하나 뽑기
        v = dq.popleft()

        print(v, end=" ")

        # i를 방문하지 않았고 v와 연결되어 있다면
        for i in range(1, n+1):
            if not visited[i] and graph[v][i]:
                dq.append(i)
                visited[i] = True


visited = [False] * (n+1)
dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)