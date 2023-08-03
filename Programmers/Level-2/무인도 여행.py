# BFS 활용
from collections import deque

def solution(maps):
    answer = []
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    visited = [[0] *  len(maps[0]) for _ in range(len(maps))]

    def bfs(x, y):
        score = int(maps[x][y])

        dq = deque()
        dq.append((x, y))

        visited[x][y] = 1

        while dq:
            x, y = dq.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                    continue
                # 현재 원소가 X가 아니고 방문한 적이 없다면 score 더해주고 deque에 추가
                if maps[nx][ny] != "X" and visited[nx][ny] == 0:
                    score += int(maps[nx][ny])
                    visited[nx][ny] = 1
                    dq.append((nx, ny))

        return score
            
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            # 현재 원소가 X가 아니고 방문한 적이 없다면 BFS 실행
            if maps[i][j] != "X" and visited[i][j] == 0:
                answer.append(bfs(i, j))
    
    if answer == []:
        return [-1]
    else:
        return sorted(answer)
    
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))