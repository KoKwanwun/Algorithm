n = int(input())
mlist = list(int(input()) for _ in range(n))
dp = [0] * n

dp[0] = mlist[0]

if(n > 1):
    dp[1] = mlist[0] + mlist[1]
if(n > 2):
    dp[2] = max(mlist[1] + mlist[2], mlist[0] + mlist[2])

# max값에 mlist[i]가 무조건 들어가기 때문에, 마지막 계단을 밟게 됨 (Silver 1 2156.포도주 시식과 다른 점)
for i in range(3, n):
    dp[i] = max(dp[i-2] + mlist[i], dp[i-3] + mlist[i-1] + mlist[i])

print(dp[n-1])