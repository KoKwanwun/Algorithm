import math

def solution(progresses, speeds):
    answer = []
    tmpAnswer = []

    # 각 작업의 배포일을 리스트로 생성
    for i in range(len(progresses)):
        workDay = math.ceil((100 - progresses[i]) / speeds[i])
        tmpAnswer.append(workDay)

    # 첫번째 배포일을 기준값으로 설정(최대 배포일, 배포 개수)
    maxWorkDay = tmpAnswer[0]
    resultValue = 1

    for i in range(1, len(tmpAnswer)):
        # 지금까지의 최대값이 현재 배포일보다 크거나 같다면 배포 개수 +1
        if(maxWorkDay >= tmpAnswer[i]):
            resultValue += 1
        # 그 외는 answer에 넣어주고, 최대 배포일, 배포 개수 초기화
        else:
            answer.append(resultValue)
            maxWorkDay = tmpAnswer[i]
            resultValue = 1

    # 마지막 배포 개수도 넣어주기
    answer.append(resultValue)

    return answer