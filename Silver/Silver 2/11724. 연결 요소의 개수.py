# 시간 초과 발생하여 input -> sys.stdin.readline() 해결
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

# bfs
def bfs(graph, n, visited):
    result = 0 

    for i in range(1, n+1):                             # 1부터 n까지 for문 실행
        if(visited[i] == False):                        # 방문하지 않았다면 실행 (연결 노드마다 실행됨)
            result += 1                                 # 연결 노드 +1

            dq = deque([i])
    
            visited[i] = True

            while dq:
                v = dq.popleft()

                for j in range(1, n+1):
                    if not visited[j] and graph[v][j]:
                        dq.append(j)
                        visited[j] = True

    return result

visited = [False] * (n+1)
print(bfs(graph, n, visited))