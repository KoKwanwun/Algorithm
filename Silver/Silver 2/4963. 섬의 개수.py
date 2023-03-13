# n, m 헷갈리지 않기
# 방향돌 때 4방향, 8방향 체크 (대각선 포함 유무)
from collections import deque
import sys

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0

    while dq:
        x, y = dq.popleft()

        for i in range(8):      # 8방향이므로 8
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))

while True:
    n, m = map(int, sys.stdin.readline().split())

    # n, m이 0이라면 break
    if n == 0 and m == 0:
        break

    # 2차원 graph 정의
    graph = []
    for _ in range(m):
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 방향 정의(대각선까지 체크)
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]

    result = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                result += 1
                bfs(i, j)

    print(result)