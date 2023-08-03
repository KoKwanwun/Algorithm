"""
다른 방식으로 graph 생성 가능
for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
"""

from collections import deque
import sys

def bfs(graph, v, visited):
    queue = deque([v])

    if visited[v] == 0:     # 0 : 방문X, 1,2 : 색
        visited[v] = 1

    while queue:
        v = queue.popleft()

        color = visited[v]
        for i in graph[v]:
            if visited[i] == 0:                 # 아직 한번도 방문하지 않음
                queue.append(i)
                if color == 1:                  # 현재의 정점과 다른 색상으로 색칠
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1 and color == 1:
                return False
            elif visited[i] == 2 and color == 2:
                return False
    return True

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n+1)

    for i in range(1, n + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(graph, i, visited)
            if not result:
                break

    print('YES' if result else 'NO')