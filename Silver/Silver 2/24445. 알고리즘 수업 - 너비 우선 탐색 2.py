import sys
from collections import deque

input = sys.stdin.readline
# 순서 변수
order = 1

def bfs(visited, graph, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    global order
    visited[R] = order  # 시작 정점 R을 방문 했다고 표시한다.
    order += 1

    dq = deque()
    dq.append(R)

    while dq:
        u = dq.popleft()
        for i in graph[u]:
            if (visited[i] == 0):
                visited[i] = order
                order += 1
                dq.append(i)

n, m, r = map(int, input().split())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순 정렬
for i in range(n+1):
    graph[i].sort(reverse = True)

bfs(visited, graph, r)
for i in range(1, n+1):
    print(visited[i])