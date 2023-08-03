from collections import deque

# bfs를 활용하여 visited의 가장 큰 값이 멀리 떨어진 노드가 됨
def bfs(graph, visited):
    dq= deque()
    dq.append(1)
    visited[1] = 1

    while dq:
        v = dq.popleft()

        for each in graph[v]:
            if visited[each] == 0:
                dq.append(each)
                visited[each] = visited[v] + 1

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for each in edge:
        graph[each[0]].append(each[1])
        graph[each[1]].append(each[0])

    visited = [False] * (n+1)

    bfs(graph, visited)

    # 가장 큰 값의 개수가 가장 멀리 떨어진 노드 개수
    return visited.count(max(visited))