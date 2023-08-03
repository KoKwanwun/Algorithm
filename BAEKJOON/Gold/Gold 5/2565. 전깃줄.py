# A의 번호를 정렬
# 앞의 B번호가 뒤의 B번호로 작다면 교차하지 않게 됨
# n에 교차하지 않는 개수를 뺀다면 없애야 하는 전깃줄의 개수를 구할 수 있음
n = int(input())
graph = []
dp = [1] * n

for _ in range(n):
    graph.append(list(map(int, input().split())))

graph.sort()

for i in range(1, n):
    for j in range(0, i):
        if graph[j][1] < graph[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))