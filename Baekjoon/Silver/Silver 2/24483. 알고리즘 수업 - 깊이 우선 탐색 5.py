# d : 노드의 깊이, , t : 방문 순서
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 순서, 결과 변수
order = 0
result = 0

def dfs(visited, graph, R, depth):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    global order, result
    order += 1
    visited[R] = order * depth  # 시작 정점 R을 방문 했다고 표시한다.
    result += visited[R]

    for i in graph[R]: # graph[R] : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[i] == -1):
            dfs(visited, graph, i, depth+1)

# 변수 입력
n, m, r = map(int, input().split())

visited = [-1] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순 정렬
for i in range(n+1):
    graph[i].sort()

dfs(visited, graph, r, 0)

print(result)