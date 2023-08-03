n, m = map(int, input().split())
dp = [1] * (n+1)

# A*m, B로 2개
if n >= m:
    dp[m] = 2

# i초에는 1초전 A쓰기, m초전 B쓰기
for i in range(m+1, n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % 1000000007

print(dp[n])