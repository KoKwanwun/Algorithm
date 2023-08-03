def solution(x, y, n):
    # float('inf') : INF
    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    
    # dp[i]는 만들 수 없는 숫자이기 때문에 continue
    # 각 해당하는 식 결과가 y보다 작거나 같을 때만 dp 갱신
    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
    
    # y가 만들 수 없는 숫자면 -1 리턴
    return -1 if dp[y] == float('inf') else dp[y]