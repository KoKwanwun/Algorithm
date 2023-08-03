import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n):
    mlist = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(mlist), 2):
        if mlist[i] == -1:
            break

        graph[mlist[0]].append([mlist[i], mlist[i+1]])

result = 0

def dfs(v, score):
    global result
    for each in graph[v]:
        if visited[each[0]] == 0:
            visited[each[0]] = 1
            result = max(result, score + each[1])
            dfs(each[0], score + each[1])
            visited[each[0]] = 0

for i in range(1, n+1):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0
print(result)