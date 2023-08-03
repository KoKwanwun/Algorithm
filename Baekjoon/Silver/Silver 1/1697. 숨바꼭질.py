from collections import deque

n, k = map(int, input().split())

# graph : 시간 담기
# visited : 방문 확인
graph = [100000] * (100001)
visited = [False] * (100001)

def dfs(graph, visited, v):
    global k
    dq = deque()
    dq.append(v)

    while dq:
        u = dq.popleft()

        # k 도달했다면 탈출
        if u == k:
            break
        
        # visited가 True라면 안해도 됨
        if visited[u] == True:
            continue
        else:
            visited[u] = True
            # 각 수치가 범위 안에 있다면 갱신
            if u-1 >= 0:
                graph[u-1] = min(graph[u]+1, graph[u-1])
                dq.append(u-1)
            if u+1 <= 100000:
                graph[u+1] = min(graph[u]+1, graph[u+1])
                dq.append(u+1)
            if 2*u <= 100000:
                graph[2*u] = min(graph[u]+1, graph[2*u])
                dq.append(2*u)

graph[n] = 0
dfs(graph, visited, n)
print(graph[k])