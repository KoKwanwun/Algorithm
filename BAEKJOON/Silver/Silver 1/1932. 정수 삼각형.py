# DP
n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 각 줄의 첫번쨰, 마지막은 위의 줄의 각각 양 끝의 원소 더하기
# 그 외는 위에 2개 중 큰 것을 더하기
for i in range(1, n):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] += graph[i-1][j]
        elif j == (len(graph[i]) - 1):
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])

print(max(graph[-1]))