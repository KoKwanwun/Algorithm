# 참고한 문제
# Kruskal 알고리즘 : 모든 정점을 최소 비용으로 연결하는 최적 해답
# 가중치 오름차순으로 정렬한 후 계산
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    link = set([costs[0][0]])
    
    while len(link) != n:
        for cost in costs:
            if cost[0] in link and cost[1] in link:
                continue
            if cost[0] in link or cost[1] in link:
                link.update([cost[0], cost[1]])
                answer += cost[2]
                break
    
    return answer