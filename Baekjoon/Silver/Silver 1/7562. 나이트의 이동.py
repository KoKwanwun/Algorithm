from collections import deque

for _ in range(int(input())):
    l = int(input())
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    graph = [[0] * l for _ in range(l)]

    dq = deque()
    dq.append((startx, starty))
    
    while dq:
        x, y = dq.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append((nx, ny))
        
        # 도착좌표라면 탈출
        if x == endx and y == endy:
            break

    print(graph[endx][endy])