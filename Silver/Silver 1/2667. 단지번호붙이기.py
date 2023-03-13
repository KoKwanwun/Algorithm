from collections import deque
import sys

n = int(sys.stdin.readline())

# 2차원 graph
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0
    count = 0

    while dq:
        x, y = dq.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위에서 벗어나거나 0인 경우 continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            # 집이 있는 곳은 dq에 넣기 (중복 방지를 위해 0으로 바꾸기)
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))

    return count

mlist = []
result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result += 1
            mlist.append(bfs(i, j))

print(result)
print(*sorted(mlist), sep="\n")         # 리스트 한줄씩 출력