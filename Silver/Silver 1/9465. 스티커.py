import sys

for _ in range(int(sys.stdin.readline())):
    n = int(input())
    dp = []
    dp.append(list(map(int, sys.stdin.readline().split())))
    dp.append(list(map(int, sys.stdin.readline().split())))

    # 두번째 열 값에 첫번째 열 대각선 값을 더해줌
    # 세번째 열부터는 전, 전전 대각선 값중 최대값을 더해주며 갱신
    if(n > 1):
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][n-1], dp[1][n-1]))