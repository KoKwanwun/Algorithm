import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
# 순서 변수
order = 1

def dfs(visited, graph, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    global order
    visited[R] = order  # 시작 정점 R을 방문 했다고 표시한다.
    order += 1

    for i in graph[R]: # graph[R] : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[i] == 0):
            dfs(visited, graph, i)

n, m, r = map(int, input().split())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(n+1):
    graph[i].sort()

dfs(visited, graph, r)
for i in range(1, n+1):
    print(visited[i])