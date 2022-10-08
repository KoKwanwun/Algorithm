def solution(board, moves):
    mlist = []
    answer = 0
    
    # 0이 아니라면 해당 인형 번호를 mlist에 추가
    def move(n):
        for i in range(len(board)):
            if board[i][n] != 0:
                mlist.append(board[i][n])
                board[i][n] = 0
                break
    
    for i in moves:
        move(i-1)
        # mlist가 1 초과(2개를 비교하기 위해)
        # -1, -2 최근 값 2개를 비교(같으면 2개 다 지우고 +2)
        if len(mlist) > 1 and mlist[-1] == mlist[-2]:
            del mlist[-1]
            del mlist[-1]
            answer += 2
    
    return answer