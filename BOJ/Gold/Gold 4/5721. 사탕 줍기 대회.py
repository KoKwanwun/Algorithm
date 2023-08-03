while True:
    m, n = map(int, input().split())
    # 탈출 조건
    if m == 0 and n == 0:
        break

    # 각 줄마다 이웃하지 않는 숫자들의 합 중 최댓값 구하기
    graph = []
    for i in range(m):
        graph.append([0] + list(map(int, input().split())))
    dp = [[0 for _ in range(n+1)] for _ in range(m)]

    for i in range(m):
        dp[i][1] = graph[i][1]

    result = [0]
    for i in range(m):
        for j in range(2, n+1):
            dp[i][j] = max(dp[i][j-1], dp[i][j-2] + graph[i][j])
        result.append(dp[i][-1])

    # 각 행의 최댓값 리스트에서 이웃하지 않는 숫자들의 합 중 최댓값 구하기
    resultDp = [0 for _ in range(m+1)]
    resultDp[1] = result[1]
    for i in range(2, m+1):
        resultDp[i] = max(resultDp[i-1], resultDp[i-2] + result[i])

    print(resultDp[-1])