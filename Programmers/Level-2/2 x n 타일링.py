def solution(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # dp에 쌓아가면서 나머지를 구하며 시간 단축
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
        
    return dp[n-1]