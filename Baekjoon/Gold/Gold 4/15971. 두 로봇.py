from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

# DFS : 36점으로 성공
# visited = [False for _ in range(n+1)]
# result = 0
# def dfs(v, sumVal, maxVal):
#     global result
#     visited[v] = True
#     if v == y:
#         result = sumVal - maxVal
#         return
    
#     for idx, lenVal in graph[v]:
#         if not visited[idx]:
#             maxVal = max(maxVal, lenVal)
#             dfs(idx, sumVal + lenVal, maxVal)
    
# dfs(x, 0, 0)
# print(result)

# BFS : 100점 성공
visited = [False for _ in range(n+1)]

dq = deque()
dq.append((x, 0, 0))
visited[x] = True
while dq:
    v, sumVal, maxVal = dq.popleft()
    if v == y:
        print(sumVal - maxVal)
        break
    for idx, lenVal in graph[v]:
        if not visited[idx]:
            visited[idx] = True
            dq.append((idx, sumVal + lenVal, max(maxVal, lenVal)))