# 플로이드 워셜은 시간초과
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))
    graph[y].append((x, c))

for _ in range(m):
    x, y = map(int, input().split())
    
    # BFS (도착 노드와 일치하면 출력하며 탈출)
    dq = deque()
    dq.append((x, 0))
    visited = [False] * (n+1)
    visited[x] = True

    while dq:
        v, d = dq.popleft()
        if v == y:
            print(d)
            break
        for i, l in graph[v]:
            if not visited[i]:
                visited[i] = True
                dq.append((i, d + l))