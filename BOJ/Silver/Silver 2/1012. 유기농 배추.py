from collections import deque

k = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# BFS
def bfs(graph, x, y):
    dq = deque()
    dq.append((x, y))

    # 큐가 빌때까지 반복
    while dq:
        # 큐에서 원소 하나 뽑기
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n or ny > m:
                continue
            if graph[nx][ny] == True:
                graph[nx][ny] = 0
                dq.append((nx, ny))

for _ in range(k):
    n, m, v = map(int, input().split())

    # 간선 정보
    graph = [[False] * (m + 1) for _ in range(n + 1)]

    for _ in range(v):
        a, b = map(int, input().split())
        graph[a][b] = True

    result = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == True:
                result += 1
                bfs(graph, i, j)

    print(result)