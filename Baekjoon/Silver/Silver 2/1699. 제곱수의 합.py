n = int(input())
# 각 수를 표현하기에 가장 큰 개수
dp = list(i for i in range(n+1))

for i in range(1, n+1):
    for j in range(1, i):
        if(j * j > i):
            break
        # 아래 조건을 한다면, 제곱수라면 1을 넣을 수 있고 표현하기에 가장 작은 개수를 구할 수 있음
        if(dp[i] > dp[i - j * j] + 1):
            dp[i] = dp[i - j * j] + 1

print(dp[n])