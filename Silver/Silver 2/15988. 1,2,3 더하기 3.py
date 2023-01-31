# DP
# 점화식 : dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
dp = [1, 2, 4]

for _ in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-1] + dp[-2] + dp[-3]) % 1000000009)
    print(dp[n-1])