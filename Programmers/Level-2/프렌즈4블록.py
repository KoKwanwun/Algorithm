from collections import deque

# 블록 기준 오른쪽, 아래, 오른쪽 아래 3방향으로 체크 후
# 다 동일하다면 checkSet에 넣기
def check(m, n, board):
    checkSet = set()
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    
    for i in range(m-1):
            for j in range(n-1):
                for k in range(3):
                    if board[i][j] == board[i + dx[k]][j + dy[k]]:
                        continue
                    break
                else:
                    checkSet.add((i, j))
                    checkSet.add((i+1, j))
                    checkSet.add((i, j+1))
                    checkSet.add((i+1, j+1))
                    
    return checkSet

# deque 활용 재정렬
# 없어진 블록 공간 위에 있는 블록으로 채우기
def arrange(board):
    for j in range(len(board[0])):
        q = deque([])

        for i in range(len(board)-1,-1,-1):
            if board[i][j] == '0':
                q.append((i,j)) 
            else:
                if q:
                    qi, qj  = q.popleft()
                    board[qi][qj] = board[i][j]
                    board[i][j] = '0'
                    q.append((i, j))

def solution(m, n, board):
    result = 0
    # 각 자리로 분류하여 리스트
    board = [list(each) for each in board]
    print(board)
    
    # 2*2를 체크한 후, 0으로 바꾸기
    # 블록 개수만큼 지워진 블록 +
    # checkSet 비우기
    while True:
        checkSet = check(m, n, board)
        
        if checkSet:
            for i, j in checkSet:
                board[i][j] = '0'
            result += len(checkSet)
            arrange(board)
            checkSet.clear()
        else:
            break
    
    return result