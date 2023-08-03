def solution(name, yearning, photo):
    answer = []
    
    for mlist in photo:
        score = 0
        for each in mlist:
            # 원소가 name에 있다면 해당하는 점수를 더해주기
            if each in name:
                score += yearning[name.index(each)]
        answer.append(score)
        
    return answer