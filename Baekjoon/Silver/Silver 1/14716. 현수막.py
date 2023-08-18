from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 8방향 설정
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0
    
    while dq:
        v, w = dq.popleft()
        
        for i in range(8):
            nx = v + dx[i]
            ny = w + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                dq.append((nx, ny))
                graph[nx][ny] = 0

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            result += 1
            bfs(i, j)
            
print(result)