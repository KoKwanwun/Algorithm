n = int(input())

# n의 최대값 30의 dp 생성
dp = [0] * 31

# n이 0일 때는 사실 경우의 수가 없지만, 점화식을 해결하기 위해 1을 넣어줌
dp[0] = 1
if(n > 1):
    dp[2] = 3

for i in range(3, n + 1):
    if(i % 2 == 0):
        dp[i] = (dp[i - 2] * 4) - (dp[i - 4])

print(dp[n])