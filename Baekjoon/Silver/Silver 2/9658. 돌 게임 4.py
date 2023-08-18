# n-1, n-3, n-4에 한 가지라도 상근이가 이기는 경우가 있다면 그 경우의 수를 선택
n = int(input())

dp = [False] * 1001
dp[2] = True
dp[4] = True
for i in range(4, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = False
    else:
        dp[i] = True

if dp[n] == 1:
    print("SK")
else:
    print("CY")