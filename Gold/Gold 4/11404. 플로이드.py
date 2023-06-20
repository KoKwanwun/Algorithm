# 플로이드 와샬 알고리즘
import sys
input = sys.stdin.readline

n = int(input())

graph = [[100001] * (n+1) for _ in range(n+1)]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

# k : 거쳐가는 정점
# i : 시작 정점
# j : 도착 정점
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 100001:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()