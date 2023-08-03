n = int(input())
mlist = list(map(int, input().split()))
dp = [0] * n

# 증가하는 수열의 최대값을 저장해나감
for i in range(n):
    for j in range(i):
        if(mlist[i] > mlist[j] and dp[i] < dp[j]):
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))