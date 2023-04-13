from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 적록색약 X
def bfs1(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[x][y] == graph[nx][ny]:
                dq.append((nx, ny))
                visited[nx][ny] = True

# 적록색약 O
def bfs2(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[x][y] == 'B':
                if graph[nx][ny] == 'B':
                    dq.append((nx, ny))
                    visited[nx][ny] = True
            else:
                if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    dq.append((nx, ny))
                    visited[nx][ny] = True

visited = [[False for _ in range(n)] for _ in range(n)]
result1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result1 += 1
            bfs1(i, j)

visited = [[False for _ in range(n)] for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result2 += 1
            bfs2(i, j)

print(result1, result2)