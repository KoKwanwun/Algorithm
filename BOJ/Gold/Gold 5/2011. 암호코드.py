mlist = list(map(int, input()))
n = len(mlist)

dp = [0] * (n + 1)
dp[0] = dp[1] = 1

# mlist[0]이 0이면 암호가 잘못됨
if(mlist[0] == 0):
    print(0)
else:
    for i in range(2, n+1):
        # 0에 해당하는 알파벳은 없기 때문에 0보다 크면 이전 dp값 더해주기
        if(mlist[i-1] > 0):
            dp[i] += dp[i-1]
        # 2자리 숫자가 10~26 범위의 숫자라면 i-2 인덱스의 dp값 더해주기
        tmp = mlist[i-2] * 10 + mlist[i-1]
        if(tmp >= 10 and tmp <= 26):
            dp[i] += dp[i-2]
    print(dp[n] % 1000000)