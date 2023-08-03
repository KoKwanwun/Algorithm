n, k = map(int, input().split())

# 이중 리스트로 dp 생성
dp = [[0] * (201) for _ in range(201)]

# 기본 틀 생성
"""
0 1 2 3 4 5 6 7 ...
0 1 2 3 4 5 6 7 ...
0 1 
0 1
0 1
0 1
0 1
...
"""
for i in range(1, 201):
    dp[i][1] = 1
    dp[1][i] = i
    dp[0][i] = i

# 점화식 : dp[i][j] = dp[i-1][j] + dp[i][j-1]에 1000000000의 나머지를 dp에 넣기
for i in range(2, n+1):
    for j in range(2, k+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[n][k])