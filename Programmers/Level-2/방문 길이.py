from collections import deque

def solution(dirs):
    # 이중 리스트와 방향 딕셔너리 생성
    visited = [[[] for _ in range(11)] for _ in range(11)]
    direction = {'U' : (0, 1), 'D' : (0, -1), 'L' : (-1, 0), 'R' : (1, 0)}
    
    result = 0
    dq = deque()
    dq.append((5, 5))           # -5, -5, 5, 5를 0, 0, 11, 11로 옮기고 중심을 (5,5)
    
    for dir in dirs:
        x, y = dq.popleft()         # 이동 전
        nx = x + direction[dir][0]  # 이동 후 x
        ny = y + direction[dir][1]  # 이동 후 y
        
        # 범위를 넘어가면 이동 전 좌표를 다시 dq에 넣기
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            dq.append((x, y))
            continue
        
        # 이동 후 visited에 이동 전 좌표가 없다면 처음 가본 길
        # result +1
        # 양쪽 좌표에 서로의 좌표 넣기 (가본 길 체크)
        if (x, y) not in visited[nx][ny]:
            result += 1
            visited[nx][ny].append((x, y))
            visited[x][y].append((nx, ny))

        # dq에 이동 후 좌표 넣기
        dq.append((nx, ny))
        
    return result

solution("ULURRDLLU")