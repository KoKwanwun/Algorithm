def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    
    # 내림차순 정렬 후, m번째 수 * m
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    
    return answer