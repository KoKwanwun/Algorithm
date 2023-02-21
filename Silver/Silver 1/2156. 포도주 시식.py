n = int(input())

mlist = list(int(input()) for _ in range(n))
dp = [0] * 10001
dp[0] = mlist[0]
if(n > 1):
    dp[1] = mlist[0] + mlist[1]
if(n > 2):
    dp[2] = max(dp[1], mlist[0] + mlist[2], mlist[1] + mlist[2])

# 경우의 수 3개 (i잔 마시지 않기, i잔만 마시기, i잔, i-1잔 마시기)
for i in range(3, n):
    dp[i] = max(dp[i-2] + mlist[i], dp[i-3] + mlist[i] + mlist[i-1], dp[i-1])

print(max(dp))