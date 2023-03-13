import sys
sys.setrecursionlimit(1000000)  # 재귀 오류 방지를 위한 범위 설정

def dfs(v):
    global result

    visited[v] = True
    cycle.append(v)
    num = nums[v]

    if visited[num] == True:
        if num in cycle:        # 다음 노드가 사이클에 있다면 사이클만큼 n에서 빼주기
            result -= len(cycle[cycle.index(num):])
        return
    else:                       # 다음 노드를 방문하지 않았다면 재귀
        dfs(num)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline());
    nums = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n+1)
    result = n

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(result)