import sys

n, m = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# dp 생성
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = graph[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 범위 누적합 리턴
# 원소 각각을 더하면 시간 초과 -> dp 활용
for _ in range(int(sys.stdin.readline())):
    i, j, x, y = map(int, sys.stdin.readline().split())
    
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])