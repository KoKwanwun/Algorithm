import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * (n) for _ in range(m)]

# 직사각형 부분은 1로 채우기
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[j][i] = 1

result = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs 사용하여 나머지 영역의 개수를 리턴
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 1
    cnt = 1

    while dq:
        x, y = dq.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if not graph[nx][ny]:
                graph[nx][ny] = 1
                dq.append((nx, ny))
                cnt += 1

    return cnt

for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))