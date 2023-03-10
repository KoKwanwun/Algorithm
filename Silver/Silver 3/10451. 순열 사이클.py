# 그래프 생성 필요없음
# 노트가 한 방향이라는 가정
import sys

# DFS
def dfs(v):
    visited[v] = True
    num = nums[v]           # num에 다음 노드 번호 넣기

    if not visited[num]:    # num에 방문하지 않았다면 대귀
        dfs(num)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    nums = [0] + list(map(int, sys.stdin.readline().split()))

    visited = [False] * (n+1)
    result = 0

    # 순열 사이클 개수 구하기
    for i in range(1, n+1):
        if not visited[i]:
            result += 1
            dfs(i)

    print(result)