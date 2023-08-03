def dfs(i, computers):
    # i의 행을 체크하는 for문
    for j in range(len(computers[i])):
        # i와 j가 같으면 방문처리
        if(i == j):
            computers[i][j] = 0
        else:
            # 연결되어 있는 곳이 있다면 방문처리한 후, 해당 행으로 이동
            if(computers[i][j] == 1):
                computers[i][j] = 0
                dfs(j, computers)

def solution(n, computers):
    result = 0

    for i in range(n):
        # i번째 행이 모두 방문처리가 되어 있다면 continue
        if(sum(computers[i]) == 0):
            continue
        dfs(i, computers)
        # 하나의 네트워크가 끝났으므로 +1 
        result += 1

    return result