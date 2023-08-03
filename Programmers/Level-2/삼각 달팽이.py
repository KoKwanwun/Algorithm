def solution(n):
    graph = [[0] * i for i in range(1, n+1)]
    maxNum = n * (n+1) / 2
    borderNum = 1
    num = 1
    idx = n

    while num <= maxNum:
        # 위에서부터 0인 인덱스 찾기 (0이 시작점)
        globalI = -1
        globalJ = -1
        for i in range(n):
            for j in range(len(graph[i])):
                if graph[i][j] == 0:
                    globalI = i
                    globalJ = j
                    break
            if globalI != -1 and globalJ != -1:
                break

        # j는 고정으로 내려가며 숫자 채우기
        for i in range(globalI, idx):
            graph[i][globalJ] = num
            num += 1

        idx -= 1

        # 맨 아랫줄 채우기
        for j in range(len(graph[idx])):
            if graph[idx][j] == 0:
                graph[idx][j] = num
                num += 1
                
        # 뒤쪽 올라가면서 숫자 채우기
        for i in range(idx-1, 0, -1):
            j = len(graph[i])-borderNum
            if j < 0:
                break
            if graph[i][j] == 0:
                graph[i][j] = num
                num += 1
                
        borderNum += 1
    
    # 결과 리스트로 만들기
    answer = []
    for element in graph:
        answer += element
    
    return answer