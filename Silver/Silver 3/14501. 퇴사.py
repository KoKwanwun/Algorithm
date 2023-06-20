# DP 활용
import sys
input = sys.stdin.readline

n = int(input())
graph = []
dp = [0 for i in range(n+1)]

for i in range(n):
    graph.append(list(map(int, input().split())))

# for문 범위 잘보기(i+graph[i][0], i이후로 상담 가능한 날)
for i in range(n):
    for j in range(i+graph[i][0], n+1):
        if dp[j] < dp[i] + graph[i][1]:
            dp[j] = dp[i] + graph[i][1]

print(dp[-1])