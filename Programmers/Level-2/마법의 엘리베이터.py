def solution(storey):
    answer = 0
    
    while storey:
        modNum = storey % 10
        
        # 6 ~ 9
        if modNum > 5:
            answer += 10 - modNum
            storey += 10
        # 0 ~ 4
        elif modNum < 5:
            answer += modNum
        # 5
        else:
            # 다음 자리수가 4보다 크다면, 10으로 가는 방법으로
            if (storey // 10) % 10 > 4:
                storey += 10
            # 그 외는 0으로 가는 방법으로
            answer += modNum
        
        storey //= 10
    
    return answer