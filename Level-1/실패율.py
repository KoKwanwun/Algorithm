def solution(N, stages):
    answer = []
    cnt = len(stages)

    for i in range(1, N+1):
        stageCnt = stages.count(i)
        
        # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
        if (stageCnt == 0):
            answer.append([i, 0])
            continue
        answer.append([i, stageCnt / cnt])
        cnt -= stageCnt

    result = []
    for each in sorted(answer, key=lambda x : -x[1]):
        result.append(each[0])

    return result