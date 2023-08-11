import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 부모, 자식 관계 설정
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# BFS
dq = deque()
dq.append(x)
visited[x] = 1

while dq:
    v = dq.popleft()
    
    # 방문한 적이 없다면 촌수 + 1
    for i in graph[v]:
        if not visited[i]:
            dq.append(i)
            visited[i] = visited[v] + 1
    
# 결과값 촌수 -1 해줘야 함 : 방문 처리로 인해 +1 되어있음
if visited[y] == 0:
    print(-1)
else:
    print(visited[y] - 1)