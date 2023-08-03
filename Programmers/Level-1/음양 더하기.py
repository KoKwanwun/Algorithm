# signs 값에 따라 값 계산(false면 -, true면 +)
def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer