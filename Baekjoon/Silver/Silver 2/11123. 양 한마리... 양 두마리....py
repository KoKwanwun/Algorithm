# visited로 방문처리를 하지 않고, #을 .으로 바꿔줌
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = []
    for _ in range(h):
        graph.append(list(input().rstrip()))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    def bfs(x, y):
        dq = deque()
        dq.append((x, y))
        graph[x][y] = '.'
        while dq:
            a, b = dq.popleft()
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx < 0 or ny < 0 or nx >= h or ny >= w:
                    continue
                if graph[nx][ny] == '#':
                    graph[nx][ny] = '.'
                    dq.append((nx, ny))
        
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '#':
                result += 1
                bfs(i, j)
                
    print(result)