N = int(input())

# graph, visited 생성
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(N)]
result = float('inf')

def back(depth, idx):
    global result
    
    # 팀원만큼 개수가 정해지면, 각 팀 전력을 구한 후 갱신
    if depth == N // 2:
        team1, team2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += graph[i][j]
        result = min(result, abs(team1 - team2))
        return

    # 조합처럼 구하기(idx부터 시작하며 중복 제거)
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            back(depth+1, i+1)
            visited[i] = False

back(0, 0)
print(result)