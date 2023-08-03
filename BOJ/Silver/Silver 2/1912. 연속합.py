n = int(input())
mlist = list(map(int, input().split()))
dp = [0] * n
dp[0] = mlist[0]

# i-1 인덱스의 값이 양수면 현재값과 더해서 dp에 넣기
# 음수라면, 현재값을 dp에 넣어줘야함 (음수만 나올 수 있기 때문에 0을 넣으면 안됨)
for i in range(1, n):
    tmp = dp[i-1] + mlist[i]
    if(dp[i-1] > 0):
        dp[i] = tmp
    else:
        dp[i] = mlist[i]

print(max(dp))