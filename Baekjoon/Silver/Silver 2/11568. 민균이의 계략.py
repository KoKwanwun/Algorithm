# LIS (Longest Increasing Sequence)
n = int(input())
mlist = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        if mlist[j] < mlist[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))