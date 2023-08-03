def solution(survey, choices):
    kind = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0} # RT CF JM AN
    score = [0,3,2,1,0,1,2,3]   # 인덱스로 불러오기 위해 인덱스 0인 값에 0을 넣어줌
    answer = []
    
    # 설문조사를 돌면서 모르겠음은 넘어감
    # 다른 것은 해당하는 점수를 딕셔너리에 더해줌
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4:
            kind[survey[i][1]] += score[choices[i]]
        else:
            kind[survey[i][0]] += score[choices[i]]
    
    # 값을 비교하여 유형 결정
    if kind["R"] < kind["T"]:
        answer.append("T")
    else:
        answer.append("R")
        
    if kind["C"] < kind["F"]:
        answer.append("F")
    else:
        answer.append("C")
        
    if kind["J"] < kind["M"]:
        answer.append("M")
    else:
        answer.append("J")
        
    if kind["A"] < kind["N"]:
        answer.append("N")
    else:
        answer.append("A")
    
    return ''.join(answer)