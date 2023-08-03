from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
def bfs(x, y):
    dq = deque()
    dq.append((x, y))

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1             # 다음 노드에 현재 노드 +1 값을 넣어 최소 칸 수 쌓아가기
                dq.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))