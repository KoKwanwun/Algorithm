# input() 시간초과, sys.stdin.readline() 통과
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n+1)]

for _ in range(n):
    graph.append([0] + list(map(int, sys.stdin.readline().split())))

# 누적합으로 변경
for i in range(1, n+1):
    for j in range(1, n+1):
        graph[i][j] += graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1]

# 식에 의해 결과값 출력
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])