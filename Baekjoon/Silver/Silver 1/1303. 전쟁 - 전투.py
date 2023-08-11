# 가로 세로 잘 확인하기
from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[False] * (m) for _ in range(n)]
resultW = 0
resultB = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            # flag : 적군 판별 변수
            flag = graph[i][j]
            cnt = 1
            visited[i][j] = True
            dq = deque()
            dq.append((i, j))
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            
            while dq:
                v, w = dq.popleft()
                
                for k in range(4):
                    nx = v + dx[k]
                    ny = w + dy[k]
                    
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    if not visited[nx][ny] and graph[nx][ny] == flag:
                        cnt += 1
                        dq.append((nx, ny))
                        visited[nx][ny] = True
                        
            if flag == "W":
                resultW += cnt * cnt
            else:
                resultB += cnt * cnt
                
print(resultW, resultB)