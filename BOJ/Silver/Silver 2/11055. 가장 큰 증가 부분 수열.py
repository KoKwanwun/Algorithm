n = int(input())
mlist = list(map(int, input().split()))
dp = [0] * n

# 증가하는 수열이라면 dp값을 넣어주고 현재 i값을 더해주기
for i in range(n):
    for j in range(i):
        if(mlist[i] > mlist[j] and dp[i] < dp[j]):
            dp[i] = dp[j]
    dp[i] += mlist[i]
    
print(max(dp))